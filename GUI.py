from UI.MainWindow import Ui_MainWindow
import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt
import json


class GUI(QtWidgets.QMainWindow):

    def __init__ (self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)