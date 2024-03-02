from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

app = Tk()
app.title("Checkboxes")
#app.iconbitmap("C:/Users/admin/Desktop/pythonimg/ugico3.ico")
#icon = PhotoImage(file = "ugico3.ico")
app.iconphoto(True, PhotoImage(file = "img5.1.png") )
app.geometry("400x400")


def show():
    lbl= Label(app, text=var.get()).pack()
#to change the value of the chekbox output we use the onvalue and offvalue syntax
var = IntVar()
c = Checkbutton(app, text="Check the box", variable=var, command=show).pack()



app.mainloop()