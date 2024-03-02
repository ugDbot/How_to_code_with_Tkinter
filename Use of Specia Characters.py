from tkinter import *
from tkinter import colorchooser
app = Tk()
app.title("Special character")
app.geometry("400x400")



#u"\u00b0" :- that is the unicode for degree, these unicodes can be googled based on what your looking for
lbl = Label(app, text="41" + u"\u00b0").pack(pady=10)

button = Button(app, text=u"\u00bb", font=("Courier, 20")).pack(pady=10)



app.mainloop()