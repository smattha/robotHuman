# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './resources/menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuWindow(object):
    def setupUi(self, menuWindow):
        menuWindow.setObjectName("menuWindow")
        menuWindow.setEnabled(True)
        menuWindow.resize(567, 596)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menuWindow.sizePolicy().hasHeightForWidth())
        menuWindow.setSizePolicy(sizePolicy)
        menuWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 142, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 142, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 142, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 213, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        menuWindow.setPalette(palette)
        menuWindow.setDocumentMode(False)
        menuWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(menuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setObjectName("menuPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.menuPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.saveMenu = QtWidgets.QPushButton(self.menuPage)
        self.saveMenu.setObjectName("saveMenu")
        self.gridLayout.addWidget(self.saveMenu, 6, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 2, 1, 1)
        self.selectExercise = QtWidgets.QComboBox(self.menuPage)
        self.selectExercise.setObjectName("selectExercise")
        self.gridLayout.addWidget(self.selectExercise, 9, 0, 1, 3)
        self.ageLabel = QtWidgets.QLabel(self.menuPage)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout.addWidget(self.ageLabel, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.menuPage)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 4)
        self.clearMenu = QtWidgets.QPushButton(self.menuPage)
        self.clearMenu.setObjectName("clearMenu")
        self.gridLayout.addWidget(self.clearMenu, 6, 0, 1, 1)
        self.descriptionTxt = QtWidgets.QTextEdit(self.menuPage)
        self.descriptionTxt.setEnabled(False)
        self.descriptionTxt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descriptionTxt.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.descriptionTxt.setObjectName("descriptionTxt")
        self.gridLayout.addWidget(self.descriptionTxt, 10, 0, 1, 3)
        self.mainImageHome = QtWidgets.QLabel(self.menuPage)
        self.mainImageHome.setMaximumSize(QtCore.QSize(240, 240))
        self.mainImageHome.setText("")
        self.mainImageHome.setScaledContents(True)
        self.mainImageHome.setAlignment(QtCore.Qt.AlignCenter)
        self.mainImageHome.setObjectName("mainImageHome")
        self.gridLayout.addWidget(self.mainImageHome, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.surnameLabel = QtWidgets.QLabel(self.menuPage)
        self.surnameLabel.setObjectName("surnameLabel")
        self.gridLayout.addWidget(self.surnameLabel, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.menuPage)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.selectExersiceButton = QtWidgets.QPushButton(self.menuPage)
        self.selectExersiceButton.setObjectName("selectExersiceButton")
        self.gridLayout.addWidget(self.selectExersiceButton, 9, 3, 1, 1)
        self.nameLabel = QtWidgets.QLabel(self.menuPage)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.menuPage)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 3, 2, 1, 1)
        self.surname = QtWidgets.QLineEdit(self.menuPage)
        self.surname.setObjectName("surname")
        self.gridLayout.addWidget(self.surname, 4, 2, 1, 1)
        self.ageTextBox = QtWidgets.QLineEdit(self.menuPage)
        self.ageTextBox.setObjectName("ageTextBox")
        self.gridLayout.addWidget(self.ageTextBox, 5, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.menuPage)
        self.ex1Page = QtWidgets.QWidget()
        self.ex1Page.setObjectName("ex1Page")
        self.stackedWidget.addWidget(self.ex1Page)
        self.ex2Page = QtWidgets.QWidget()
        self.ex2Page.setObjectName("ex2Page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ex2Page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget.addWidget(self.ex2Page)
        self.ex3Page = QtWidgets.QWidget()
        self.ex3Page.setObjectName("ex3Page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.ex3Page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget.addWidget(self.ex3Page)
        self.ex4Page = QtWidgets.QWidget()
        self.ex4Page.setObjectName("ex4Page")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.ex4Page)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.stackedWidget.addWidget(self.ex4Page)
        self.ex5Page = QtWidgets.QWidget()
        self.ex5Page.setObjectName("ex5Page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ex5Page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget.addWidget(self.ex5Page)
        self.ex6Page = QtWidgets.QWidget()
        self.ex6Page.setObjectName("ex6Page")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.ex6Page)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.stackedWidget.addWidget(self.ex6Page)
        self.feeback = QtWidgets.QWidget()
        self.feeback.setObjectName("feeback")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.feeback)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_10.setVerticalSpacing(30)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.feedbackEasyButton = QtWidgets.QPushButton(self.feeback)
        self.feedbackEasyButton.setObjectName("feedbackEasyButton")
        self.gridLayout_10.addWidget(self.feedbackEasyButton, 2, 0, 1, 1)
        self.nornal = QtWidgets.QWidget(self.feeback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nornal.sizePolicy().hasHeightForWidth())
        self.nornal.setSizePolicy(sizePolicy)
        self.nornal.setObjectName("nornal")
        self.gridLayout_10.addWidget(self.nornal, 1, 1, 1, 1)
        self.hard = QtWidgets.QWidget(self.feeback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hard.sizePolicy().hasHeightForWidth())
        self.hard.setSizePolicy(sizePolicy)
        self.hard.setObjectName("hard")
        self.gridLayout_10.addWidget(self.hard, 1, 2, 1, 1)
        self.feedbackNormalButton = QtWidgets.QPushButton(self.feeback)
        self.feedbackNormalButton.setObjectName("feedbackNormalButton")
        self.gridLayout_10.addWidget(self.feedbackNormalButton, 2, 1, 1, 1)
        self.feedbackHardButton = QtWidgets.QPushButton(self.feeback)
        self.feedbackHardButton.setObjectName("feedbackHardButton")
        self.gridLayout_10.addWidget(self.feedbackHardButton, 2, 2, 1, 1)
        self.terminateButton = QtWidgets.QPushButton(self.feeback)
        self.terminateButton.setObjectName("terminateButton")
        self.gridLayout_10.addWidget(self.terminateButton, 3, 0, 1, 1)
        self.easy = QtWidgets.QWidget(self.feeback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.easy.sizePolicy().hasHeightForWidth())
        self.easy.setSizePolicy(sizePolicy)
        self.easy.setObjectName("easy")
        self.gridLayout_10.addWidget(self.easy, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.feeback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 0, 1, 1, 1)
        self.nextExersice = QtWidgets.QPushButton(self.feeback)
        self.nextExersice.setObjectName("nextExersice")
        self.gridLayout_10.addWidget(self.nextExersice, 3, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.feeback)
        self.ex5Step2 = QtWidgets.QWidget()
        self.ex5Step2.setObjectName("ex5Step2")
        self.label_11 = QtWidgets.QLabel(self.ex5Step2)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 881, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.go2Home = QtWidgets.QPushButton(self.ex5Step2)
        self.go2Home.setGeometry(QtCore.QRect(350, 250, 251, 121))
        self.go2Home.setObjectName("go2Home")
        self.stackedWidget.addWidget(self.ex5Step2)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.ex5Answer2 = QtWidgets.QWidget(self.page_2)
        self.ex5Answer2.setObjectName("ex5Answer2")
        self.gridLayout_14.addWidget(self.ex5Answer2, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ex5Answer1 = QtWidgets.QWidget(self.page_2)
        self.ex5Answer1.setObjectName("ex5Answer1")
        self.horizontalLayout_6.addWidget(self.ex5Answer1)
        self.gridLayout_14.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.answer1Ex3 = QtWidgets.QPushButton(self.page_2)
        self.answer1Ex3.setObjectName("answer1Ex3")
        self.gridLayout_14.addWidget(self.answer1Ex3, 1, 0, 1, 1)
        self.answer2Ex3 = QtWidgets.QPushButton(self.page_2)
        self.answer2Ex3.setObjectName("answer2Ex3")
        self.gridLayout_14.addWidget(self.answer2Ex3, 1, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.answer1Exersice4 = QtWidgets.QPushButton(self.page)
        self.answer1Exersice4.setGeometry(QtCore.QRect(180, 610, 89, 25))
        self.answer1Exersice4.setObjectName("answer1Exersice4")
        self.answer2Exersice4 = QtWidgets.QPushButton(self.page)
        self.answer2Exersice4.setGeometry(QtCore.QRect(420, 610, 89, 25))
        self.answer2Exersice4.setObjectName("answer2Exersice4")
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(110, 40, 721, 561))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.exercise4Answer1 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.exercise4Answer1.setScaledContents(True)
        self.exercise4Answer1.setObjectName("exercise4Answer1")
        self.horizontalLayout_17.addWidget(self.exercise4Answer1)
        self.exercise4Answer2 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.exercise4Answer2.setScaledContents(True)
        self.exercise4Answer2.setObjectName("exercise4Answer2")
        self.horizontalLayout_17.addWidget(self.exercise4Answer2)
        self.exercise4Answer3 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.exercise4Answer3.setScaledContents(True)
        self.exercise4Answer3.setObjectName("exercise4Answer3")
        self.horizontalLayout_17.addWidget(self.exercise4Answer3)
        self.label_39 = QtWidgets.QLabel(self.page)
        self.label_39.setGeometry(QtCore.QRect(10, 40, 881, 20))
        self.label_39.setText("")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.answer3Exersice4 = QtWidgets.QPushButton(self.page)
        self.answer3Exersice4.setGeometry(QtCore.QRect(660, 610, 89, 25))
        self.answer3Exersice4.setObjectName("answer3Exersice4")
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        menuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuMove_to_Activity = QtWidgets.QMenu(self.menuWindows)
        self.menuMove_to_Activity.setObjectName("menuMove_to_Activity")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        menuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menuWindow)
        self.statusbar.setObjectName("statusbar")
        menuWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(menuWindow)
        self.toolBar.setObjectName("toolBar")
        menuWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAAbout = QtWidgets.QAction(menuWindow)
        self.actionAAbout.setObjectName("actionAAbout")
        self.actionActivity_1 = QtWidgets.QAction(menuWindow)
        self.actionActivity_1.setObjectName("actionActivity_1")
        self.actionActivity_2 = QtWidgets.QAction(menuWindow)
        self.actionActivity_2.setObjectName("actionActivity_2")
        self.actionActivity_3 = QtWidgets.QAction(menuWindow)
        self.actionActivity_3.setObjectName("actionActivity_3")
        self.actionActivity_4 = QtWidgets.QAction(menuWindow)
        self.actionActivity_4.setObjectName("actionActivity_4")
        self.actionActivity_5 = QtWidgets.QAction(menuWindow)
        self.actionActivity_5.setObjectName("actionActivity_5")
        self.actionActivity_6 = QtWidgets.QAction(menuWindow)
        self.actionActivity_6.setObjectName("actionActivity_6")
        self.actionMain_Menu = QtWidgets.QAction(menuWindow)
        self.actionMain_Menu.setObjectName("actionMain_Menu")
        self.actionExport_Data = QtWidgets.QAction(menuWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionMedia_Files_Folder = QtWidgets.QAction(menuWindow)
        self.actionMedia_Files_Folder.setObjectName("actionMedia_Files_Folder")
        self.menu.addAction(self.actionExport_Data)
        self.menuSetting.addAction(self.actionMedia_Files_Folder)
        self.menuMove_to_Activity.addAction(self.actionActivity_1)
        self.menuMove_to_Activity.addAction(self.actionActivity_2)
        self.menuMove_to_Activity.addAction(self.actionActivity_3)
        self.menuMove_to_Activity.addAction(self.actionActivity_4)
        self.menuMove_to_Activity.addAction(self.actionActivity_5)
        self.menuMove_to_Activity.addAction(self.actionActivity_6)
        self.menuWindows.addAction(self.menuMove_to_Activity.menuAction())
        self.menuWindows.addAction(self.actionMain_Menu)
        self.menuHelp.addAction(self.actionAAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(menuWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(menuWindow)

    def retranslateUi(self, menuWindow):
        _translate = QtCore.QCoreApplication.translate
        menuWindow.setWindowTitle(_translate("menuWindow", "Αρχική οθόνη "))
        self.textEdit.setHtml(_translate("menuWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\',\'sans-serif\'; font-size:24pt; color:#8ab4f8;\">Εκπαιδευτική εφαρμογή</span></p></body></html>"))
        self.saveMenu.setText(_translate("menuWindow", "Αποθήκευση"))
        self.ageLabel.setText(_translate("menuWindow", "Ηλικία"))
        self.label.setText(_translate("menuWindow", "Διαθέσιμες επιλογές"))
        self.clearMenu.setText(_translate("menuWindow", "Εκκαθάριση"))
        self.surnameLabel.setText(_translate("menuWindow", "Επίθετο"))
        self.label_2.setText(_translate("menuWindow", "Προσωπικά στοιχεία"))
        self.selectExersiceButton.setText(_translate("menuWindow", "Έναρξη"))
        self.nameLabel.setText(_translate("menuWindow", "Όνομα"))
        self.feedbackEasyButton.setText(_translate("menuWindow", "Εύκολος"))
        self.feedbackNormalButton.setText(_translate("menuWindow", "-"))
        self.feedbackHardButton.setText(_translate("menuWindow", "Δυσκολός"))
        self.terminateButton.setText(_translate("menuWindow", "Τερματισμός"))
        self.label_6.setText(_translate("menuWindow", "Πόσο εύκολος σου φάνηκε ο γρίφος"))
        self.nextExersice.setText(_translate("menuWindow", "Επόμενη δραστηριότητα"))
        self.label_11.setText(_translate("menuWindow", "Τέλος"))
        self.go2Home.setText(_translate("menuWindow", "Αρχικό Μενού"))
        self.answer1Ex3.setText(_translate("menuWindow", "A"))
        self.answer2Ex3.setText(_translate("menuWindow", "B"))
        self.answer1Exersice4.setText(_translate("menuWindow", "A"))
        self.answer2Exersice4.setText(_translate("menuWindow", "B"))
        self.exercise4Answer1.setText(_translate("menuWindow", "TextLabel"))
        self.exercise4Answer2.setText(_translate("menuWindow", "TextLabel"))
        self.exercise4Answer3.setText(_translate("menuWindow", "TextLabel"))
        self.answer3Exersice4.setText(_translate("menuWindow", "Γ"))
        self.menu.setTitle(_translate("menuWindow", "File"))
        self.menuEdit.setTitle(_translate("menuWindow", "Edit"))
        self.menuSetting.setTitle(_translate("menuWindow", "Setting"))
        self.menuWindows.setTitle(_translate("menuWindow", "Windows"))
        self.menuMove_to_Activity.setTitle(_translate("menuWindow", "Move to Activity"))
        self.menuAbout.setTitle(_translate("menuWindow", "About"))
        self.menuHelp.setTitle(_translate("menuWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("menuWindow", "toolBar"))
        self.actionAAbout.setText(_translate("menuWindow", "About"))
        self.actionActivity_1.setText(_translate("menuWindow", "Activity 1"))
        self.actionActivity_2.setText(_translate("menuWindow", "Activity 2"))
        self.actionActivity_3.setText(_translate("menuWindow", "Activity 3"))
        self.actionActivity_4.setText(_translate("menuWindow", "Activity 4"))
        self.actionActivity_5.setText(_translate("menuWindow", "Activity 5"))
        self.actionActivity_6.setText(_translate("menuWindow", "Activity 6"))
        self.actionMain_Menu.setText(_translate("menuWindow", "Main Menu"))
        self.actionExport_Data.setText(_translate("menuWindow", "Export Data"))
        self.actionMedia_Files_Folder.setText(_translate("menuWindow", "Media Files Folder"))
