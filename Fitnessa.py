from PySide2 import QtWidgets, QtGui, QtCore 
import myfitnesspal
from MainWindow import MainWindow




class Fitnessa():
    def __init__(self, username, password):
        self.client = myfitnesspal.Client(username, password)
        self.main_window = MainWindow()
