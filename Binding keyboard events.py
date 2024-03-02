from tkinter import *
from tkinter import ttk
app = Tk()
app.geometry("400x400")
app.title("Keyboard events")

def clicker(event):
    #str(event.x) and str(event.y) this returns the x and y position of the mouse on the app in string form
    #event.char shows which key you pressed
    #event.keysym shows the symbol
    #We pass the event word to initialize the binding
    myLabel = Label(app, text="You clicked a button"  + " " + event.char)
    myLabel.pack(pady=20)

myButton = Button(app, text="click me", command=clicker)
#bind the keyboard attribute using <> then put in the key e.g: Button-1 for Left mouse,
#Button-3 for right mouse and Enter for whenever the mouse in on the widget or Leave for when it leaves
#Return is for enter key
#Keys is any key on the keyboard
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)

#===================================BINDING DROPDOWN BOXES AND COMBO BOXES==========================
#create list for the boxes
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thrsday",
    "Friday",
    "Saturday",
    "Sunday",
]

def selected(event):
    myLabel = Label(app, text=clicked.get()).pack()
def comboclick(event):
    myLabel = Label(app, text=myCombo.get()).pack()


clicked = StringVar()
clicked.set(options[0])

drop_down_box = OptionMenu(app, clicked, *options, command=selected)
drop_down_box.pack(pady=20)

myCombo = ttk.Combobox(app, value=options)
#set the initial text on the combobox============
myCombo.current(0)
#======================================
myCombo.bind("<<ComboboxSelected>>", comboclick )
myCombo.pack()



app.mainloop()