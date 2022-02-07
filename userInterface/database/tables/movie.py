from sqlalchemy import Column, String, Integer

from base import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __init__(self, title):
        self.title = title