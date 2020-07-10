from UI.MainWindow import Ui_MainWindow
import datetime
import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt
import json


class GUI(QtWidgets.QMainWindow):

    def __init__ (self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Default parameters
        self.ui.tabs.setCurrentIndex(0)




    def set_weight(self, weight, unit):
        w = str(weight)
        self.ui.weightL.setText()
    



    def set_sleep_time(self, hours, unit):
        h = str(hours)
        self.ui.sleepTimeL.setText("{} {}".format(h, unit))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = GUI()
    GUI.show()
    sys.exit(app.exec_())