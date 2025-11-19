from models import Customer, Account, Transaction

def test_customer_creation(session):
    cust = Customer(name="Alice", email="alice@example.com")
    session.add(cust)
    session.commit()

    assert cust.id is not None
    assert cust.name == "Alice"
    assert cust.email == "alice@example.com"

def test_account_creation_and_balance(session):
    cust = Customer(name="Bob", email="bob@example.com")
    session.add(cust)
    session.commit()

    acct = Account(account_number="AC123", balance=100.0, customer_id=cust.id)
    session.add(acct)
    session.commit()

    assert acct.id is not None
    assert acct.balance == 100
    assert acct.customer_id == cust.id

def test_account_deposit(session):
    cust = Customer(name="Klara", email="klara@example.com")
    session.add(cust)
    session.commit()

    acct = Account(account_number="AC199", balance=50.0, customer_id=cust.id)
    session.add(acct)
    session.commit()

    acct.deposit(100.0)
    session.commit()

    assert acct.balance == 150.0

def test_account_withdrawn(session):
    cust = Customer(name="Eve", email="eve@example.com")
    session.add(cust)
    session.commit()

    acct = Account(account_number="AC324", balance=50.0, customer_id=cust.id)
    session.add(acct)
    session.commit()

    try:
        acct.withdraw(100.0)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Insufficient Funds"

def test_transaction_creation(session):
    cust = Customer(name='Alex', email='alex@example.com')
    session.add(cust)
    session.commit()

    acct = Account(account_number="ACC688", balance=60.0, customer_id=cust.id)
    session.add(acct)
    session.commit()

    txn = Transaction(account_id="ACC688", type="deposit", description="Initial Deposit", amount=50.0)
    session.add(txn)
    session.commit()

    assert txn.id is not None
    assert txn.amount == 50.0
    assert txn.description == "Initial Deposit"