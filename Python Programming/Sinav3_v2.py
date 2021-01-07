from tkinter import *
import tkinter.messagebox
class MyGUI:
    def _init_(self):
        self.pen = Tk()
        self.pen.title("Temperature Conversion")
        self.lbl1=Label(self.pen,text="Value of Temperature: ").grid(row="0",column="0")
        self.veri=IntVar()
        self.entry1 = Entry(self.pen, textvariable=self.veri).grid(row="0", column="1")
        self.lbl2 = Label(self.pen, text="Check the scale: ").grid(row="1", column="0")
        self.radiovar=IntVar()
        self.radio1 = Radiobutton(self.pen, text="Celsius",variable=self.radiovar,value=1).grid(row="1", column="1")
        self.radio2 = Radiobutton(self.pen, text="Fahrenheit",variable=self.radiovar,value=2).grid(row="2", column="1")
        self.hespla= Button(self.pen,text="Convert",command=self.hesapla).grid(row="3", column="0",columnspan="2")
        self.pen.mainloop()

    def hesapla(self):
        if self.radiovar.get() == 1:
            sayi=self.veri.get()
            celcius=(5/9)*(sayi-32)
            tkinter.messagebox.showinfo("Result", str(celcius)+" Celcius")
        elif self.radiovar.get() == 2:
            sayi=self.veri.get()
            print(sayi)
            fahrenheit=((9/5)*(sayi)+32)
            tkinter.messagebox.showinfo("Result", str(fahrenheit)+" Fahrenheit")
        else:
            tkinter.messagebox.showerror("Error", "Select a scale")
MyGUI()