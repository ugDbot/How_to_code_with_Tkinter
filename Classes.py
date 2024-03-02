from tkinter import *

app = Tk()
app.geometry("400x400")
app.title("Classes")

class UG:
    #this functions is called when your class runs
    def __init__(self, master):
        #__init__ means initialize
        myFrame = Frame(master)
        myFrame.pack()
        #when calling widgets we have to pass self
        self.myButton = Button(master, text="Click Me!", command =self.clicker)
        self.myButton.pack()
    def clicker(self):
        print("Worked")

u = UG(app)

app.mainloop()