from PySide2 import QtWidgets, QtGui, QtCore 
import myfitnesspal
from GUI import GUI
import time
import datetime
from threading import Thread




class Fitnessa():
    def __init__(self, username, password):
        self.client = myfitnesspal.Client(username = username, password = password)
        self.ui = GUI()
        self.mfp_client = None
        



    def pull_fitness_data(self):
        DELAY = 1 # minutes
        while True:
            self.update_gui()
            time.sleep(DELAY * 60)
        



    def update_gui(self):
        datetime_today = datetime.date.today()
        night_sleep = self.client.get_measurements("Night Sleep (hours)", datetime_today).popitem(last = False)
        nap = self.client.get_measurements("Nap (hours)", datetime_today).popitem(last = False)
        total_sleep = night_sleep[1] + nap[1]
        self.ui.set_sleep_time(total_sleep, "hours")
        #self.ui.set_weight()
        print(night_sleep)
        print(nap)



    def start(self):
        self.ui.show()
        self.update_thread = Thread(target=self.pull_fitness_data, daemon=True)
        self.update_thread.start()
