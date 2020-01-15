import tkinter as tk
import myfitnesspal
import json



class Page(tk.Frame):
    def __init__(self):
        supeer().__init__(master)
        self.master = master
    
    def create_widgets(self):
            
"""
Places for labels and buttons:
    grid size: 20 by 30
    ----page home----
    prev_button: 0-3 x 0-6
    next_button: 0-3 x 24-30
"""

def get_account()
    with open("account_info.json", "r") as info_file:
        json.load(info_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
