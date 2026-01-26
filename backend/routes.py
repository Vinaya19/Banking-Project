from flask import Blueprint, request, jsonify
from models import db
from services import BankService
from models import Customer, Account, Transaction

bp = Blueprint('api', __name__)

@bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    cust = BankService.create_customer(data['name'], data['email'])
    response = jsonify(cust.to_dict())
    return response, 201

@bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    email = (data.get('email') or '').strip().lower()
    name = (data.get('name') or '').strip().lower()

    if not email:
        return jsonify({"message": "Email is required"}), 400

    cust = BankService.get_or_create_customer(email, name)
    return jsonify(cust.to_dict()), 200

@bp.route('/customers/<int:customer_id>/accounts', methods=['GET'])
def get_customer_accounts(customer_id):
    accounts = BankService.get_customer_accounts(customer_id)
    return jsonify([acct.to_dict() for acct in accounts]), 200

@bp.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    acct = BankService.create_account(data['customer_id'], data.get('initial_deposit', 0.0))
    return jsonify(acct.to_dict()), 201

@bp.route('/accounts/<int:account_id>/deposit', methods=['POST'])
def deposit(account_id):
    data = request.json
    txn = BankService.deposit(account_id, float(data['amount']), data.get('description'))
    return jsonify(txn.to_dict()), 200

@bp.route('/accounts/<int:account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
    data = request.json
    txn = BankService.withdraw(account_id, float(data['amount']), data.get('description'))
    return jsonify(txn.to_dict()), 200

@bp.route('/accounts/<int:account_id>/transfer', methods=['POST'])
def transfer(account_id):
    data = request.json
    txn1, txn2 = BankService.transfer(account_id, data['to_account_number'], data['amount'], data.get('description'))
    return jsonify({'from': txn1.to_dict(), 'to': txn2.to_dict()}), 200

@bp.route('/accounts/<int:account_id>/transactions', methods=['GET'])
def transactions(account_id):
    txns = BankService.get_transactions(account_id)
    return jsonify([t.to_dict() for t in txns]), 200