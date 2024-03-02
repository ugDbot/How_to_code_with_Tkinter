from tkinter import *
from tkinter import filedialog
import os

app=Tk()
app.title("Open external programs")
app.geometry("400x400")

def open_program():
    my_program = filedialog.askopenfilename()
    #to open program:
    os.system('"%s"'  % my_program)

my_button = Button(app, text="Open program", command=open_program)
my_button.pack(pady=20)


app.mainloop()