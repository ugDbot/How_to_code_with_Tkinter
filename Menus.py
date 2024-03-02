from tkinter import *
from tkinter import ttk
app = Tk()
app.geometry("400x400")
app.title("Menus")

myMenu = Menu(app)
app.configure(menu=myMenu)

def clicked():
    pass
def file_new():
    file_new_frame.pack(fill="both", expand=1)

#create a menu item
file_menu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

#create an edit menu item
edit_menu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=clicked)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=clicked)

#===============================================USING FRAMES WITH MENUS==============================================

#create some frames
file_new_frame = Frame(app, width=400, height=400, bg="red")





app.mainloop()