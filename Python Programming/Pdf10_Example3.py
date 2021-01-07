from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btnOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btnCancel = Button(window, text = "Cancel", fg = "yellow", command = self.processCancel)
        btnOK.pack()
        btnCancel.pack()
        window.mainloop()

    def processOK(self):
        print("Ok button is clicked")

    def processCancel(self):
        print("Cancle button is clicked")

ProcessButtonEvent()