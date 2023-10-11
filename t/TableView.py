from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView
from PyQt5.QtGui import QIcon
import datetime
from PyQt5 import QtCore,Qt, QtGui, QtWidgets
from PyQt5.QtGui import * 

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

class TableView():
    def __init__(self, ui, data,header):
        self.data = data


        self.table1 = QTableWidget(ui)


        self.setData()
        self.table1.setHorizontalHeaderLabels(header)
        self.table1.resizeColumnsToContents()
        self.table1.resizeRowsToContents()
        
 
    def setData(self): 
        numrows = len(self.data)  
        numcols = len(self.data[0])  

        self.table1.setColumnCount(numcols)
        self.table1.setRowCount(numrows)
        
        for row in range(numrows):
                for column in range(numcols):
                    # Check if value datatime, if True convert to string 
                    if isinstance(self.data[row][column], datetime.datetime):
                        self.table1.setItem(row, column, QTableWidgetItem((self.data[row][column].strftime('%d/%m/%Y %H:%M:%S'))))
                    else:
                        self.table1.setItem(row, column, QTableWidgetItem((self.data[row][column])))
        self.table1.show()
        self.table1.setGeometry(QtCore.QRect(400,300, 1000,600))
        self.table1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        # self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        fontId = QFontDatabase.addApplicationFont("fonts/Mansalva.ttf")
        if fontId < 0:
            print('font not loaded')
        else :
            families = QtGui.QFontDatabase.applicationFontFamilies(fontId)
            font = QtGui.QFont(families[0])
            self.table1.setFont(font)
            self.table1.setStyleSheet(" font-size: 22pt; " )

            stylesheet = "::section{Background-color:rgb(255,204,229)}"
            self.table1.horizontalHeader().setStyleSheet(stylesheet)
            self.table1.verticalHeader().setStyleSheet(stylesheet)
            # self.table1.setScr
            
            header = self.table1.horizontalHeader()
            # header.setResizeMode(QHeaderView.Re)
            header.setStretchLastSection(True)