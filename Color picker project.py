from tkinter import *
from tkinter import colorchooser
app = Tk()
app.title("Color Picker")
app.geometry("400x400")

def color():
    #function to call color app...the list[] is because the output comes out in a list where [1] is the hashcode of the color which the system can read
    my_color = colorchooser.askcolor()[1]
    label = Label(app, text=my_color).pack(pady=20)
    label2 = Label(app, text="You picked a color", bg=my_color).pack(pady=20)

button = Button(app, text="My color", command=color).pack(pady=20)



app.mainloop()