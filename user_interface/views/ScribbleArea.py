from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from sqlalchemy import false
from views.ui.menu import Ui_menuWindow
from views.ui.dialog import Ui_Dialog
from PyQt5 import  QtWidgets,QtGui
from PyQt5.QtWidgets import (QAction, QApplication, QColorDialog, QFileDialog,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QImage, QImageWriter, QPainter, QPen, qRgb

class ScribbleArea(QWidget):
    def __init__(self,imagePath ,parent=None):
        super(ScribbleArea, self).__init__()

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 2
        self.myPenColor = Qt.red
        self.image = QImage()
        self.lastPoint = QPoint()
        self.imagePath=imagePath
        self.openImage3(imagePath)
        self.counter=0

    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False

        newSize = loadedImage.size().expandedTo(self.size())
        # self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        # self.image.scaled(3000,3000,1)
        self.imagePath=fileName
        self.update()
        return True

    def openImage3(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False

        newSize = loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.image.scaled(3000,3000,1)
        self.imagePath=fileName
        self.update()
        return True

    def openImage2(self, fileName):
        loadedImage = QImage()
        newSize = loadedImage.size().expandedTo(self.size())
        # self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.image.scaled(self.curSize,1)
        self.imagePath=fileName
        self.update()
        return True


    def setController(self,controller):
        self.controller=controller

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    # def mouseMoveEvent(self, event):
    #     if (event.buttons() & Qt.LeftButton) and self.scribbling:
    #         self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling:
            self.drawEclipse(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    def resizeEvent(self, event):
            self.openImage(self.imagePath)
        # if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width() + 128, self.image.width())
            newHeight = max(self.height() + 128, self.image.height())
            self.image.scaled(self.width(),self.height())
            self.resizeImage(self.image, event.size())
            self.curSize=event.size()
            # QSize(newWidth, newHeight))
            self.update()
    def resize(self):
            self.openImage(self.imagePath)
        # if self.width() > self.image.width() or self.height() > self.image.height():
            # newWidth = max(self.width() + 128, self.image.width())
            # newHeight = max(self.height() + 128, self.image.height())
            # self.image.scaled(newWidth,newHeight,1)
            self.resizeImage(self.image, self.size())
            # QSize(newWidth, newHeight))
            self.update()
        # super(ScribbleArea, self).resizeEvent(event)

    # def drawLineTo(self, endPoint):
        # painter = QPainter(self.image)
        # painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
        #         Qt.RoundCap, Qt.RoundJoin))
        # painter.drawLine(self.lastPoint, endPoint)
        # self.modified = True

        # rad = self.myPenWidth / 2 + 2
        # self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        # self.lastPoint = QPoint(endPoint)

    def drawEclipse(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                Qt.RoundCap, Qt.RoundJoin))
        painter.drawEllipse(self.lastPoint, 10,10)
        self.modified = True

        rad = self.myPenWidth / 2 + 2
        self.update()
        self.lastPoint = QPoint(endPoint)    
        self.controller.storeAnswer(1)
        self.controller.storePose(endPoint)
        
    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QImage(newSize, QImage.Format_RGB32)
        imagen=image.scaled(newSize)
        painter = QPainter(image)
        painter.drawImage(QPoint(0, 0), imagen)
        self.image = image

        # loadedImage = QImage()
        # loadedImage.load('/home/smatt/Documents/git/src/resources/images/ex5/image.png')
        
        # newSize = loadedImage.size().expandedTo(self.size())
        # self.image = loadedImage
        


    def print_(self):
        printer = QPrinter(QPrinter.HighResolution)

        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth
        


