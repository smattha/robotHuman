# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
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
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1190, 734))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.answer3Img = QtWidgets.QLabel(self.widget)
        self.answer3Img.setObjectName("answer3Img")
        self.gridLayout_5.addWidget(self.answer3Img, 4, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.answer2 = QtWidgets.QPushButton(self.widget)
        self.answer2.setObjectName("answer2")
        self.gridLayout_5.addWidget(self.answer2, 6, 3, 1, 1)
        self.descriptionBox = QtWidgets.QLabel(self.widget)
        self.descriptionBox.setObjectName("descriptionBox")
        self.gridLayout_5.addWidget(self.descriptionBox, 1, 2, 1, 5, QtCore.Qt.AlignHCenter)
        self.answer4 = QtWidgets.QPushButton(self.widget)
        self.answer4.setObjectName("answer4")
        self.gridLayout_5.addWidget(self.answer4, 6, 5, 1, 1)
        self.mainImage = QtWidgets.QLabel(self.widget)
        self.mainImage.setMaximumSize(QtCore.QSize(700, 500))
        self.mainImage.setScaledContents(True)
        self.mainImage.setObjectName("mainImage")
        self.gridLayout_5.addWidget(self.mainImage, 2, 2, 1, 5, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.answer1 = QtWidgets.QPushButton(self.widget)
        self.answer1.setObjectName("answer1")
        self.gridLayout_5.addWidget(self.answer1, 6, 2, 1, 1)
        self.answer2Img = QtWidgets.QLabel(self.widget)
        self.answer2Img.setObjectName("answer2Img")
        self.gridLayout_5.addWidget(self.answer2Img, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.answer4Img = QtWidgets.QLabel(self.widget)
        self.answer4Img.setObjectName("answer4Img")
        self.gridLayout_5.addWidget(self.answer4Img, 4, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.answer5 = QtWidgets.QPushButton(self.widget)
        self.answer5.setObjectName("answer5")
        self.gridLayout_5.addWidget(self.answer5, 6, 6, 1, 1)
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout_5.addWidget(self.name, 0, 2, 1, 5)
        self.answer3 = QtWidgets.QPushButton(self.widget)
        self.answer3.setObjectName("answer3")
        self.gridLayout_5.addWidget(self.answer3, 6, 4, 1, 1)
        self.answer1Img = QtWidgets.QLabel(self.widget)
        self.answer1Img.setObjectName("answer1Img")
        self.gridLayout_5.addWidget(self.answer1Img, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 2, 7, 1, 1)
        self.answer5Img = QtWidgets.QLabel(self.widget)
        self.answer5Img.setObjectName("answer5Img")
        self.gridLayout_5.addWidget(self.answer5Img, 4, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.Results = QtWidgets.QLabel(self.widget)
        self.Results.setAlignment(QtCore.Qt.AlignCenter)
        self.Results.setObjectName("Results")
        self.gridLayout_5.addWidget(self.Results, 3, 2, 1, 5)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.answer3Img.setText(_translate("Form", "Image 3"))
        self.answer2.setText(_translate("Form", "B"))
        self.descriptionBox.setText(_translate("Form", "TextLabel"))
        self.answer4.setText(_translate("Form", "Δ"))
        self.mainImage.setText(_translate("Form", "TextLabel"))
        self.answer1.setText(_translate("Form", "A"))
        self.answer2Img.setText(_translate("Form", "Image 2"))
        self.answer4Img.setText(_translate("Form", "Image 4"))
        self.answer5.setText(_translate("Form", "Ε"))
        self.name.setText(_translate("Form", "Δραστηριότητα"))
        self.answer3.setText(_translate("Form", "Γ"))
        self.answer1Img.setText(_translate("Form", "Image 1"))
        self.answer5Img.setText(_translate("Form", "Image 5"))
        self.Results.setText(_translate("Form", "Απαντήσεις"))
