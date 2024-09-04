import hashlib
import random

import pandas as pd

from entities import Account, Transaction, Transaction_log


def random_account_id() -> str:
    return ''.join(map(lambda x : str(x).zfill(4), [random.randint(4005, 6900), random.randint(50, 7000), random.randint(50, 7000)]))


def random_account_holder_name() -> str:
    return hashlib.sha256(''.join([chr(random.randint(65,90)) for _ in range(7)]).encode('utf-8')).hexdigest()


def create_account(logger, session):
    account_id = random_account_id()
    account_holder_name = random_account_holder_name()
    
    def verify(account_id):
        result = session.query(Account.account_id).where(Account.account_id == account_id).all()
        if result:
            return False
        
        return True
    
    while not verify(account_id):
        account_id = random_account_id()
        account_holder_name = random_account_holder_name()
    
    
    new_account = Account(account_id=account_id, account_holder_name=account_holder_name, account_balance=0)
    session.add(new_account)
    session.commit()
    
    logger.info('INSERT Account(id={}, name={}, balance={})'.format(account_id, account_holder_name, 0))
    return


def create_transaction(logger, session):
    account_id_list = session.query(Account.account_id).all()
    if not account_id_list:
        logger.info('RETURN CREATE_TRANSACTION: DATA LENGTH IS ZERO')
        return
    
    selected_account_id = random.choice(account_id_list)[0]
    amount = random.randint(0,9) * (10 ** random.randint(0,7))
    transaction_type = ['withdraw', 'deposit'][random.randint(0,1)]
    
    prev_account_balance = session.query(Account.account_balance).where(Account.account_id == selected_account_id).all()[0][0]
    
    timestamp = pd.Timestamp.now()
    next_account_balance = 0
    event = None
    
    if transaction_type == 'withdraw':
        if amount > prev_account_balance:
            new_log = Transaction_log(transaction_id=None, date=timestamp, event='Failed')
            session.add(new_log)
            session.commit()
            return
        else:
            event = 'Success'
            next_account_balance = prev_account_balance - amount
    elif transaction_type == 'deposit':
        event = 'Success'
        next_account_balance = prev_account_balance + amount
    else:
        raise NotImplementedError
    
    session.query(Account).where(Account.account_id == selected_account_id).update({'account_balance': next_account_balance})
    new_transaction = Transaction(date=timestamp, account_id=selected_account_id, amount=amount, type=transaction_type)
    session.add(new_transaction)
    session.commit()
    
    new_log = Transaction_log(transaction_id=new_transaction.id ,date=timestamp, event=event)
    session.add(new_log)
    session.commit()
    
    logger.info('INSERT Transaction(date={}, account_id={}, amount={}, type={})'.format(timestamp, selected_account_id, amount, transaction_type))
    return
