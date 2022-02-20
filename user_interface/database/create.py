#!/usr/bin/python3
#https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
from datetime import date


from base import Session, engine, Base
from tables.movie import Movie
from tables.actor import Actor

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()


# 2 - generate database schema
Base.metadata.create_all(engine)
