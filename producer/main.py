import time
import logging
import argparse

import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from functions import create_account, create_transaction
from entities import Base

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dbuser', default='postgres', type=str, help='postgresql db user')
    parser.add_argument('--password', default='postgres', type=str, help='postgresql db password')
    parser.add_argument('--host', default='localhost', help='postgresql host address')
    parser.add_argument('--port', default=5432, type=int, help='postgresql host port')
    parser.add_argument('--dbname', default='postgres', type=str, help='postgresql database name')
    
    args = parser.parse_args()
    
    engine = create_engine(url=f'postgresql://{args.dbuser}:{args.password}@{args.host}:{args.port}/{args.dbname}')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    logger.info('CREATE TABLES ACCOUNT, BANK_TRANSACTION, TRANSACTION_LOG')
    
    while 1:
        task = ['create_account', 'create_transaction'][np.random.choice(np.arange(2),size=1,p=[0.3, 0.7])[0]]
        if task == 'create_account':
            create_account(logger, session)
            logger.info('RUN CREATE_ACCOUNT')
        else:
            create_transaction(logger, session)
            logger.info('RUN CREATE_TRANSACTION')
        time.sleep(0.5)
