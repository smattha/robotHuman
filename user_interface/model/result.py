from sqlalchemy import Column, String, Integer

from base import Base


class Result(Base):
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


