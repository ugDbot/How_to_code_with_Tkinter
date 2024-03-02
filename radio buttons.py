from tkinter import *
from PIL import ImageTk,Image
app=Tk()
app.title("Radio buttons")
app.iconbitmap('C:/Users/admin/Pictures/company.ico')
MODES = [
    ("Pepper", "Pepper"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),

]

food = StringVar()
food.set("Pepper")

for text, mode in MODES:
    Radiobutton(app, text=text, variable=food, value=mode).pack(anchor=W)

def click(value):
    my_label = Label(app, text=value)
    my_label.pack()

#Radiobutton(app, text="Option1", variable=g, value=1, command=lambda: click(g.get())).pack()
#Radiobutton(app, text="Option2", variable=g, value=2, command=lambda: click(g.get())).pack()

#my_label = Label(app, text=food.get()).pack()

button_1 = Button(app, text="Click", command=lambda: click(food.get()))
button_1.pack()








app.mainloop()