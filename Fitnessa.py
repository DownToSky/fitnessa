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
        self.fitness_data = dict()
        

    def pull_fitness_data(self):
        DELAY = 10 #minutes
        while True:
            datetime_today = datetime.datetime.now()
            self. fitness_data = self.client.get_date(datetime_today)
            print(self.fitness_data)
            time.sleep(DELAY * 60)
        

    def start(self):
        self.ui.show()
        self.update_thread = Thread(target=self.pull_fitness_data, daemon=True)
        self.update_thread.start()
