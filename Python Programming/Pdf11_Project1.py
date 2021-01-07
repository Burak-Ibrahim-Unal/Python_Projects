from tkinter import * # Import all definitions from tkinter

class Calculator:
    def __init__(self,wdw):
        self.frame1=Frame(wdw)
        self.frame1.pack()
        Label(self.frame1,text='Value1= ').grid(row=0,column=0)
        self.entry1=Entry(self.frame1)
        self.entry1.grid(row=0,column=1)
        self.label2=Label(self.frame1,text='Value2')
        self.label2.grid(row=1,column=0)
        self.entry2=Entry(self.frame1)
        self.entry2.grid(row=1,column=1)
        self.frame2=Frame(wdw)
        self.frame2.pack()
        self.frame3=Frame(wdw)
        self.frame3.pack()
        self.label3=Label(self.frame3,text='')
        self.label3.grid(row=2,column=0)
        b=0
        for i in ['+','-','*','/']:
            Button(self.frame2,text=i,command=
                   lambda a=i:self.calc(a)).grid(row=3,column=b, padx=5,pady=10)
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
            elif op=='/':
                result=e1/e2
            self.label3['text']='Result ='+ format(result,'0.2f')
        except ValueError:
            self.label3['text']='Value error'
        except ZeroDivisionError:
            self.label3['text']="You cant divide by zero!!!"

    def main():
        t=Tk()
        t.title('Calculator')
        c = Calculator(t)
        t.mainloop()

    main()