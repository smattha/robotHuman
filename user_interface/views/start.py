# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/start.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.uiStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.uiStart.setObjectName("uiStart")
        self.gridLayout.addWidget(self.uiStart, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.visionStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.visionStop.setObjectName("visionStop")
        self.gridLayout.addWidget(self.visionStop, 1, 2, 1, 1)
        self.s2tStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.s2tStop.setObjectName("s2tStop")
        self.gridLayout.addWidget(self.s2tStop, 5, 2, 1, 1)
        self.visionStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.visionStart.setObjectName("visionStart")
        self.gridLayout.addWidget(self.visionStart, 1, 1, 1, 1)
        self.t2sStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.t2sStop.setObjectName("t2sStop")
        self.gridLayout.addWidget(self.t2sStop, 7, 2, 1, 1)
        self.trainingStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.trainingStart.setObjectName("trainingStart")
        self.gridLayout.addWidget(self.trainingStart, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.startAll = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startAll.setObjectName("startAll")
        self.gridLayout.addWidget(self.startAll, 0, 1, 1, 1)
        self.robotFaceStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.robotFaceStart.setObjectName("robotFaceStart")
        self.gridLayout.addWidget(self.robotFaceStart, 4, 1, 1, 1)
        self.trainingStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.trainingStop.setObjectName("trainingStop")
        self.gridLayout.addWidget(self.trainingStop, 10, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.motorStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.motorStart.setObjectName("motorStart")
        self.gridLayout.addWidget(self.motorStart, 6, 1, 1, 1)
        self.motorStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.motorStop.setObjectName("motorStop")
        self.gridLayout.addWidget(self.motorStop, 6, 2, 1, 1)
        self.stopAll = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stopAll.setObjectName("stopAll")
        self.gridLayout.addWidget(self.stopAll, 0, 2, 1, 1)
        self.s2tStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.s2tStart.setObjectName("s2tStart")
        self.gridLayout.addWidget(self.s2tStart, 5, 1, 1, 1)
        self.uiStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.uiStop.setObjectName("uiStop")
        self.gridLayout.addWidget(self.uiStop, 3, 2, 1, 1)
        self.t2sStart = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.t2sStart.setObjectName("t2sStart")
        self.gridLayout.addWidget(self.t2sStart, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.robotFaceStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.robotFaceStop.setObjectName("robotFaceStop")
        self.gridLayout.addWidget(self.robotFaceStop, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuMotor = QtWidgets.QMenu(self.menubar)
        self.menuMotor.setToolTip("")
        self.menuMotor.setObjectName("menuMotor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOffine = QtWidgets.QAction(MainWindow)
        self.actionOffine.setObjectName("actionOffine")
        self.menuMotor.addAction(self.actionOffine)
        self.menubar.addAction(self.menuMotor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Motor"))
        self.label_5.setText(_translate("MainWindow", "UI"))
        self.uiStart.setText(_translate("MainWindow", "Start"))
        self.label_4.setText(_translate("MainWindow", "Training"))
        self.visionStop.setText(_translate("MainWindow", "Stop"))
        self.s2tStop.setText(_translate("MainWindow", "Stop"))
        self.visionStart.setText(_translate("MainWindow", "Start"))
        self.t2sStop.setText(_translate("MainWindow", "Stop"))
        self.trainingStart.setText(_translate("MainWindow", "Start"))
        self.label_6.setText(_translate("MainWindow", "Text2Speech"))
        self.startAll.setText(_translate("MainWindow", "Start All"))
        self.robotFaceStart.setText(_translate("MainWindow", "Start"))
        self.trainingStop.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "Robot Face"))
        self.motorStart.setText(_translate("MainWindow", "Start"))
        self.motorStop.setText(_translate("MainWindow", "Stop"))
        self.stopAll.setText(_translate("MainWindow", "Stop All"))
        self.s2tStart.setText(_translate("MainWindow", "Start"))
        self.uiStop.setText(_translate("MainWindow", "Stop"))
        self.t2sStart.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Vision"))
        self.robotFaceStop.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Speech2Text"))
        self.menuMotor.setTitle(_translate("MainWindow", "Motor"))
        self.actionOffine.setText(_translate("MainWindow", "Offine"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
