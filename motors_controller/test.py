from PyQt5 import QtCore, QtGui, QtDesigner
from views.motor import Ui_MainWindow;


class App(QApplication):
    def __init__(self,):
        super(App, self).__init__(sys_argv)

    def dump_ui(widget, path):
        builder = QtDesigner.QFormBuilder()
        stream = QtCore.QFile(path)
        stream.open(QtCore.QIODevice.WriteOnly)
        builder.save(stream, widget)
        stream.close()

# app = QtGui.QApplication([''])

# dialog = QtGui.QDialog()
# Ui_Dialog().setupUi(dialog)

ui = Ui_MainWindow()
ui.setupUi()

ui.show()
    




if __name__ == '__main__':
    try:
        app = App(sys.argv)
        app.exec_()
        dump_ui(ui, 'myui.ui')

        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)
