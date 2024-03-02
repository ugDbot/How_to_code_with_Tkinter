from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

app = Tk()
app.title("Drop down box")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")
app.geometry("400x400")

def show():
    lbl = Label(app, text=clicked.get()).pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


# set the default value on the drop down box to be shown
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(app, clicked, *options)
drop.pack()

mybtn = Button(app, text="show", command=show).pack()






app.mainloop()