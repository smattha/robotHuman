# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './resources/page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1210, 754)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 0, 1, 5)
        self.answer2 = QtWidgets.QPushButton(self.widget)
        self.answer2.setObjectName("answer2")
        self.gridLayout_5.addWidget(self.answer2, 5, 1, 1, 1)
        self.answer4 = QtWidgets.QPushButton(self.widget)
        self.answer4.setObjectName("answer4")
        self.gridLayout_5.addWidget(self.answer4, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 5)
        self.answer5 = QtWidgets.QPushButton(self.widget)
        self.answer5.setObjectName("answer5")
        self.gridLayout_5.addWidget(self.answer5, 5, 4, 1, 1)
        self.testing = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testing.sizePolicy().hasHeightForWidth())
        self.testing.setSizePolicy(sizePolicy)
        self.testing.setObjectName("testing")
        self.gridLayout_5.addWidget(self.testing, 3, 0, 1, 5)
        self.answer1 = QtWidgets.QPushButton(self.widget)
        self.answer1.setObjectName("answer1")
        self.gridLayout_5.addWidget(self.answer1, 5, 0, 1, 1)
        self.answer3 = QtWidgets.QPushButton(self.widget)
        self.answer3.setObjectName("answer3")
        self.gridLayout_5.addWidget(self.answer3, 5, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Απαντήσεις"))
        self.answer2.setText(_translate("Form", "B"))
        self.answer4.setText(_translate("Form", "Δ"))
        self.label_3.setText(_translate("Form", "Δραστηριότητα 1"))
        self.answer5.setText(_translate("Form", "Ε"))
        self.answer1.setText(_translate("Form", "A"))
        self.answer3.setText(_translate("Form", "Γ"))
