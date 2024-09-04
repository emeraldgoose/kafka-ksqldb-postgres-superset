from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'

    account_id = Column(String, primary_key=True, nullable=False)
    account_holder_name = Column(String, nullable=False)
    account_balance = Column(Integer, nullable=False)


class Transaction(Base):
    __tablename__ = "bank_transaction"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    account_id = Column(String, ForeignKey(Account.account_id), nullable=False)
    amount = Column(Integer, nullable=False)
    type = Column(String, nullable=False)


class Transaction_log(Base):
    __tablename__ = 'transaction_log'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    transaction_id = Column(Integer, ForeignKey(Transaction.id), nullable=True)
    date = Column(TIMESTAMP, nullable=False)
    event = Column(String, nullable=False)