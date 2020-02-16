from PySide2 import QtWidgets, QtGui, QtCore 
import myfitnesspal
import sys
import json



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("Fitnessa")
    
    def create_widgets(self):
        pass

def get_account():
    with open("account_info.json", "r") as info_file:
        json.load(info_file)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.resize(800,600)
    window.show()

    sys.exit(app.exec_())
