from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
path='/home/stergios/git/src/robotHuman/user_interface'
engine = create_engine('sqlite:///'+path+'/database/scheme/mysqlList.db')
Session = sessionmaker(bind=engine)


Base = declarative_base()

