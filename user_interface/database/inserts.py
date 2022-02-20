#!/usr/bin/python3
#https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
from datetime import date


from base import Session, engine, Base
from tables.movie import Movie
from tables.actor import Actor


# 3 - create a new session
session = Session()

# 4 - create movies
bourne_identity = Movie("The Bourne Identity")

actor = Actor("The Bourne Identity")


# 9 - persists data
session.add(bourne_identity)
session.add(actor)


# 10 - commit and close session
session.commit()



movies = session.query(Movie).all()

# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title}')
print('')

session.close()