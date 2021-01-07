from tkinter import *
from tkinter import messagebox
class MyProgram:
    def __init__(self):
        windows=Tk()
        Label(windows,text='Value of').grid(row=0,column=0)
        self.datum=IntVar()
        Entry(windows,textvariable=self.datum).grid(row=0,column=1,columnspan=1)
        Label(windows,text='Check Scale:').grid(row=1,column=0)
        self.value=IntVar()
        Radiobutton(windows,text='C',variable=self.value,value=1).grid(row=1,column=1)
        Radiobutton(windows,text='F',variable=self.value,value=2).grid(row=1,column=2)
        Button(windows,text='Submit',command=self.process).grid(row=2,column=0,columnspan=2)
        windows.mainloop()

    def process(self):
        if self.value.get()==1:
            result=(5/9*(self.datum.get()-32))
        else:
            result=(9/5*self.datum.get()+32)

    showinfo("Result",result)