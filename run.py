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
    app = QtWidgets.QApplication(sys.argv)
    username, password = get_account()
    fitnessa = Fitnessa(username, password)

    fitnessa.start()
    sys.exit(app.exec_())