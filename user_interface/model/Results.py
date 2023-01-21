

from collections import namedtuple
from os.path import exists
from sqlalchemy import Column, String, Integer
from sqlalchemy import Column, String, Integer

from model.base import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine

class Results(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    name = Column(String)
    age = Column(String)
    surname = Column(String)

    answerEx1 = Column(String)
    answerEx2 = Column(String)
    answerEx3 = Column(String)
    answerEx4 = Column(String)
    answerEx5A = Column(String)
    answerEx5B = Column(String)
    answerEx6A = Column(String)
    answerEx6B = Column(String)

    answerEx7 = Column(String)
    answerEx8 = Column(String)
    answerEx9 = Column(String)
    answerEx10 = Column(String)
    answerEx11A = Column(String)
    answerEx11B = Column(String)
    answerEx12A = Column(String)
    answerEx12B = Column(String)

    feedbackE1 = Column(String)
    feedbackE2 = Column(String)
    feedbackE3 = Column(String)
    feedbackE4 = Column(String)
    feedbackE5 = Column(String)
    feedbackE6 = Column(String)
    feedbackE7 = Column(String)
    feedbackE8 = Column(String)
    feedbackE9 = Column(String)
    feedbackE10 = Column(String)
    feedbackE11 = Column(String)
    feedbackE12 = Column(String)



    def __init__(self):
        self.title = ''
        self.name = ''
        self.age = ''
        self.surname = ''

        self.answerEx1 = ''
        self.answerEx2 = ''
        self.answerEx3 = ''
        self.answerEx4 = ''
        self.answerEx5A = ''
        self.answerEx5B = ''
        self.answerEx6A = ''
        self.answerEx6B = ''

        self.answerEx7 = ''
        self.answerEx8 = ''
        self.answerEx9 = ''
        self.answerEx10 = ''
        self.answerEx11A = ''
        self.answerEx11B = ''
        self.answerEx12A = ''
        self.answerEx12B = ''

        self.feedbackE1 = ''
        self.feedbackE2 = ''
        self.feedbackE3 = ''
        self.feedbackE4 = ''
        self.feedbackE5 = ''
        self.feedbackE6 = ''
        self.feedbackE7 = ''
        self.feedbackE8 = ''
        self.feedbackE9 = ''
        self.feedbackE10 = ''
        self.feedbackE11 = ''
        self.feedbackE12 = ''


