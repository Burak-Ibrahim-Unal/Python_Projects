from tkinter import *

class ProcessButton():
    def __init__(self):
        window=Tk()
        
        btnOK=Button(window,text="OK",fg="blue",command=self.processOK)
        btnCancel=Button(window,text="Cancel",fg="purple",command=self.processCancel)

        btnOK.pack()
        btnCancel.pack()

        window.mainloop()

    def processOK(self):
        print("pressed OK button")

    def processCancel(self):
        print("pressed Cancel button")

ProcessButton()
