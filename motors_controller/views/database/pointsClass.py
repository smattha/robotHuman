from xxlimited import Str
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem
# from views.ui.menu import Ui_menuWindow
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)
# from views.DisplayImage import DisplayImageWidget
# from views.page1View import page1View
# from views.page2View import page2View
from views.motor import Ui_MainWindow;
from threading import Thread
import time




import json
from turtle import position
from PyQt5.QtCore import QObject, pyqtSignal
from sqlalchemy import true
import json
from collections import namedtuple
from os.path import exists
from sqlalchemy import Column, String, Integer
from sqlalchemy import Column, String, Integer

from views.base import Base
# from base import Session, engine, Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from threading import Thread


class pointsClass(Base):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True)

    motorA = Column(String)
    motorB = Column(String)
    motorC = Column(String)
    motorD = Column(String)
    motorE = Column(String)
    motorF = Column(String)
    name = Column(String)

