from tkinter import *

def processOk():
    print("Pressed Ok button")

def processCancel():
    print("Pressed cancel button")

window=Tk()

btnOk=Button(window,text="OK",fg="red",bg="yellow",command=processOk)
btnCancel=Button(window,text="CANCEL",fg="blue",bg="yellow",command=processCancel)

btnOk.pack()
btnCancel.pack()

window.mainloop()