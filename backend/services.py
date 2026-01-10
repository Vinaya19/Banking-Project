from models import db, Customer, Account, Transaction
#from sqlalchemy.exc import IntegrityError
import random

class BankService:

    @staticmethod
    def create_customer(name: str, email: str) -> Customer:
        cust = Customer(name=name, email=email)
        db.session.add(cust)
        db.session.commit()
        return cust
    
    @staticmethod
    def create_account(customer_id: int, initial_deposit: float = 0.0) -> Account:
        acct_num = BankService._generate_account_number()
        acct = Account(account_number=acct_num, balance=0.0, customer_id=customer_id)
        db.session.add(acct)
        db.session.flush()

        if initial_deposit > 0:
            acct.deposit(initial_deposit)
            txn = Transaction(account_id=acct.id, type="deposit", amount=initial_deposit, 
                              description='initial deposit')
            db.session.add(txn)
        db.session.commit()
        return acct
    
    @staticmethod
    def _generate_account_number() -> str:
        return 'AC' + str(random.randint(1000000, 99999999))
    
    @staticmethod
    def deposit(account_id: str, amount: float, description: str = None):
        account = Account.query.get(account_id)
        if not account:
            raise ValueError('Account not found')
        account.deposit(amount)
        txn = Transaction(account_id=account.id, type="deposit", amount=amount, 
                          description=description or 'Deposit')
        db.session.add(txn)
        db.session.commit()
        return txn
    
    @staticmethod
    def withdraw(account_id: str, amount: float, description: str = None):
        account = Account.query.get(account_id)
        if not account:
            raise ValueError('Account not found')
        account.withdraw(amount)
        txn = Transaction(account_id=account.id, type='withdraw', amount=amount, 
                          description=description or 'Withdraw')
        db.session.add(txn)
        db.session.commit()
        return txn
    
    @staticmethod
    def transfer(from_account_id: int, to_account_num: str, amount: float, description: str = None):
        from_acct = Account.query.get(from_account_id)
        if not from_acct:
            raise ValueError('Source account not found')
        to_acct = Account.query.filter_by(account_number=to_account_num).first()
        if not to_acct:
            raise ValueError('Destination account not found')
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        
        from_acct.withdraw(amount)
        to_acct.deposit(amount)
        txn1 = Transaction(account_id=from_acct.id, type='withdraw', amount=amount, 
                          description=description or f'Transfer from {from_acct.account_number}')
        txn2 = Transaction(account_id=to_acct.id, type="deposit", amount=amount, 
                          description=description or f'Transfer to {to_acct.account_number}')
        db.session.add_all([txn1, txn2])
        db.session.commit()
        return txn1, txn2
    
    @staticmethod
    def get_transactions(account_id: int, limit: int = 50):
        return Transaction.query.filter_by(account_id=account_id).order_by(Transaction.created_at.desc()).limit(limit).all()
    
    @staticmethod
    def get_customer_accounts(customer_id: int):
        return Account.query.filter_by(customer_id=customer_id)