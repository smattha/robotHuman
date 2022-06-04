from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:////home/stergios/git/src/robotHuman/user_interface/database/scheme/mysqlList.db')
Session = sessionmaker(bind=engine)


Base = declarative_base()

