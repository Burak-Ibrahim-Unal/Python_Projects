from tkinter import *

class Calculator:
    def __init__(self,window):
        self.frame1=Frame(window)
        self.frame1.pack()
        Label(self.frame1,text='Value1 =').grid(row=0,column=0)
        self.entry1=Entry(self.frame1)
        self.entry1.grid(row=0,column=1)
        self.label2=Label(self.frame1,text='Value2= ')
        self.label2.grid(row=1,column=0)

        self.entry2 = Entry(self.frame1)
        self.entry2.grid(row=1,column=1)

        self.frame2=Frame(window)
        self.frame2.pack()

        self.frame3=Frame(window)
        self.frame3.pack()
        self.label3=Label(self.frame3,text='')
        self.label3.grid(row=2,column=0)

        b=0
        for i in ['+','-','*','/']:
            Button(self.frame2, text=i, command=
                   lambda b=i: self.calc(b)).grid(row=3,column=b, padx=5, pady=10)
            b+=1

    def calc(self,op):
        try:
            e1=float(self.entry1.get())
            e2=float(self.entry2.get())

            if op=='+':
                result=e1+e2
            elif op=='-':
                result=e1-e2
            elif op=='*':
                result=e1*e2
            elif op== '/':
                result=e1/e2
            self.label3['text']='Result = '+format(result,'0.2f') #+format(round(result,2)
        except ValueError:
            self.label3['text']='Value Error'
        except ZeroDivisionError:
            self.label3['text']='You cant divide zero'

def main():
    t=Tk()
    t.title('Calculator')
    Calculator(t)
    t.mainloop()

main()




