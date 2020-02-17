from PySide2 import QtWidgets, QtGui, QtCore 
import myfitnesspal
import sys
import json
from Fitnessa import Fitnessa


ACCOUNT_FILE = "account.json"

def get_account():
    username, password = None, None
    with open(ACCOUNT_FILE, "r") as info_file:
        acc_info = json.load(info_file)
        username = acc_info["username"]
        password = acc_info["password"]
    return username, password


if __name__ == "__main__":
    username, password = get_account()
    app = QtWidgets.QApplication([])
    fitnessa = Fitnessa(username, password)
    fitnessa.main_window.resize(800, 600)
    fitnessa.main_window.show()

    sys.exit(app.exec_())
