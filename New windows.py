from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

app = Tk()
app.title("New windows")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")



def open():
    global my_img
    top = Toplevel()
    top.title("2nd window")
    top.iconbitmap("C:/Users/admin/Pictures/company.ico")
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img1.jpg"))
    lbl = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close window", command = top.destroy).pack()

btn = Button(app, text="Open 2nd window", command = open).pack()

app.mainloop()