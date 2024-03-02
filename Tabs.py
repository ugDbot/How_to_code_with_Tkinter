from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Tabs")
app.geometry("400x400")
my_notebook = ttk.Notebook(app)
my_notebook.pack()


def hide():
    #tabs are listed like a python list, hence our list starts from 0-1,2,3...
    my_notebook.hide(1)
def show():
    my_notebook.add(my_frame2, text="Red tab")





my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=2)

my_notebook.add(my_frame1, text="Blue tab")
my_notebook.add(my_frame2, text="Red tab")



my_button = Button(my_frame1, text="hide tab 2", command=hide).pack(pady=10)


my_button2 = Button(my_frame2, text="hide tab 1", command=show).pack(pady=10)








app.mainloop()