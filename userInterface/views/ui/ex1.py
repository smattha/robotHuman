# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 706)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 721, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap("resources/images/test.jpg"))
        self.mainImage.setScaledContents(True)
        self.mainImage.setObjectName("mainImage")
        self.verticalLayout.addWidget(self.mainImage)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(23, 490, 711, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.answer1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.answer1.setObjectName("answer1")
        self.horizontalLayout_2.addWidget(self.answer1)
        self.answer2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.answer2.setObjectName("answer2")
        self.horizontalLayout_2.addWidget(self.answer2)
        self.answer3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.answer3.setObjectName("answer3")
        self.horizontalLayout_2.addWidget(self.answer3)
        self.answer4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.answer4.setObjectName("answer4")
        self.horizontalLayout_2.addWidget(self.answer4)
        self.answer5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.answer5.setObjectName("answer5")
        self.horizontalLayout_2.addWidget(self.answer5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.answer1.setText(_translate("Form", "a"))
        self.answer2.setText(_translate("Form", "b"))
        self.answer3.setText(_translate("Form", "c"))
        self.answer4.setText(_translate("Form", "d"))
        self.answer5.setText(_translate("Form", "e"))
