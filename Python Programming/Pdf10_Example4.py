from tkinter import *

class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title("Widgets Demo") # Set a title
        frame1 = Frame(window) # Create a frame
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", # Create a check button
        variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
        variable = self.v2, value = 1,
        command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text = "Red", bg = "yellow",
        variable = self.v2, value = 2,
        command = self.processRadiobutton)
        cbtBold.grid(row = 1, column = 1) # Grid manager
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name) # Create entry
        btGetName = Button(frame2, text = "Get Name",
        command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo") #Create message
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        text = Text(window) # Create text
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")
        window.mainloop()
    def processCheckbutton(self):
        print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked")) # Check button status
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") # Radio button status
    + "is selected ")
    def processButton(self):
        print("Your name is " + self.name.get())
WidgetsDemo()