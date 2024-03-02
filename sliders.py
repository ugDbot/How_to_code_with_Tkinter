from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

app = Tk()
app.title("Sliders")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")
app.geometry("400x400")


def slide(var):
    lbl = Label(app, text=horizontal.get()).pack()
    app.geometry(str(horizontal.get()) + str(vertical.get()))


horizontal = Scale(app, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

vertical = Scale(app,from_=0, to=400)
vertical.pack()

btn = Button(app, text="Click me", command=slide).pack()




app.mainloop()
