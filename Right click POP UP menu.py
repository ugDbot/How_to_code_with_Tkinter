from tkinter import *

# How to create a right click or any binding menu popup

app = Tk()
app.title("Right click pop up menu")
app.geometry("400x400")


def hello():
    pass


def hi():
    pass


def hey():
    pass


def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)


# Create a menu
my_menu = Menu(app, tearoff=False)
my_menu.add_command(label="Say Hello", command=hello)
my_menu.add_command(label="Say Hi", command=hi)
my_menu.add_command(label="Say hey", command=hey)

app.bind("<Button-3>", my_popup)

app.mainloop()
