from tkinter import *
from tkinter import messagebox
from random import randint


class Rb:
    def __init__(self,root):
        label=Label(root,text='Amount of Money')
        label.grid(row=0,column=0)
        e1=IntVar()
        e1.set('')
        entry1=Entry(root,textvariable=e1)
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        self.var= IntVar()
        for text, value in [('EUR',1),('USD',2),('JPY',3),('GBP',4)]:
            Radiobutton(root,text=text,value=value,variable=self.var,command=
                        lambda a=e1,b=text:self.fun(a,b)).grid(row=value,column=0,padx=5,pady=5,sticky=W)

    def fun(self,am,t):
        i=self.var.get()
        if(i==1):
            zl=4.3
        elif(i==2):
            zl=3.75
        elif(i==3):
            zl=0.03
        else:
            zl=4.80

        messagebox.showinfo(str(am.get())+' '+t+' is ',format(zl*am.get(),'0.2f')+'zl')

def main():
    t=Tk()
    t.title('Currency Exchanger')
    t.geometry('300x200')
    rb=Rb(t)
    t.mainloop()

main()