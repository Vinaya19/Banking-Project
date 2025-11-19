from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    accounts = db.relationship('Account', backref='customer', lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(30), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    transactions = db.relationship('Transaction', backref='account', lazy=True)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdraw amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient Funds')
        self.balance -= amount

    def to_dict(self):
        return {"id": self.id, "account_number": self.account_number, "balance": self.balance, 
                "customer_id": self.customer_id}


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {"id": self.id, "account_id": self.account_id, "type": self.type, "amount": self.amount, 
                "description": self.description, "created_at": self.created_at.isoformat()}