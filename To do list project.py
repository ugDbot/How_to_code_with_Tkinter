from tkinter import *
from tkinter import filedialog
import pickle

app = Tk()
app.title("To do list")
app.geometry("500x500")

#create frame
my_frame = Frame(app)
my_frame.pack(pady=10)

#create list box
my_list = Listbox(my_frame, width=80, height=5, bg="SystemButtonFace",#the default color of most tkinter apps
                  bd=2, fg="#464646", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

stuff = ["Walk the dog", "but grocies", "buy maps"]
#Add dummy list to list box
for item in stuff:
    my_list.insert(END, item)
"""
#create scrollbar
my_scroll = Scrollbar(my_frame)
my_scroll.pack(side=RIGHT, fill=BOTH)

#add scrollbar
my_list.config(yscrollcommand=my_scroll.set)
my_scroll.config(command=my_list.yview)"""

#create horizontal scrollbar
my_scroll2 = Scrollbar(my_frame)
my_scroll2.pack(side=BOTTOM, fill=X)

#add horizontal scrollbar
my_list.config(xscrollcommand=my_scroll2.set)
my_scroll2.config(orient = HORIZONTAL, command=my_list.xview)


#create entry box
my_entry = Entry(app, width=100)
my_entry.pack(pady=20)

#create button frame
btn_frame = Frame(app)
btn_frame.pack(pady=20)

#functions
def delete():
    my_list.delete(ANCHOR)
def add():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
def cross():
    my_list.itemconfig(my_list.curselection(), fg="red")
    my_list.selection_clear(0, END)
def uncross():
    my_list.itemconfig(my_list.curselection(), fg="#464646")
    my_list.selection_clear(0, END)
def delete_crossed():
    count = 0
    while count < my_list.size(): #this loops the items in our list and numbers them
        if my_list.itemcget(count, "fg") == "red": #this gets the information the things in our list and if the fg equals red...
            my_list.delete(my_list.index(count))#delete it
        else:
            count += 1
def save_list():
    file_name = filedialog.asksaveasfilename(initialdir= "C:/Users/admin/Documents", title="Save File",
                                             filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        #delete crossed off items before saving
        count = 0
        while count < my_list.size():  # this loops the items in our list and numbers them
            if my_list.itemcget(count,
                                "fg") == "red":  # this gets the information the things in our list and if the fg equals red...
                my_list.delete(my_list.index(count))  # delete it
            else:
                count += 1
        #grab everything in our list
        stuff = my_list.get(0, END)
        #Open the file
        output_file = open(file_name, "wb")

        #add the stuff to the file
        pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(initialdir= "C:/Users/admin/Documents", title="Open File",
                                             filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        #Delete any list currently open
        my_list.delete(0, END)

        #Open the file
        input_file = open(file_name, "rb")

        #load the data from the file
        stuff = pickle.load(input_file)

        #output stuff to the list
        for item in stuff:
            my_list.insert(END, item)

def clear_list():
    my_list.delete(0, END)
#create menu
my_menu = Menu(app)
app.config(menu=my_menu)

#add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

#add drop down items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

#add some buttons
delete_btn = Button(btn_frame, text="Delete item", command=delete)
add_btn = Button(btn_frame, text="Add item", command=add)
cross_btn = Button(btn_frame, text="Cross off item", command=cross)
uncross_btn = Button(btn_frame, text="Uncross item", command=uncross)
uncross2_btn = Button(btn_frame, text="Deleted crossed", command=delete_crossed)

delete_btn.grid(row=0, column=0)
add_btn.grid(row=0, column=1, padx=20)
cross_btn.grid(row=0, column=2, padx=20)
uncross_btn.grid(row=0, column=3, padx=20)
uncross2_btn.grid(row=0, column=4, padx=20)









app.mainloop()