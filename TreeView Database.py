from tkinter import *
from tkinter import ttk
from tkinter.tix import *  # Balloon tip module

app = Tk()
app.title("TreeView")
app.geometry("500x600")

# initiate the tipper balloon
tip = Balloon(app)

# tree view frame
tree_frame = Frame(app)
tree_frame.pack(pady=10)

# Tree view scroll bar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
my_tree.pack()

# configure the scroll bar
tree_scroll.config(command=my_tree.yview)

# define our columns
my_tree["columns"] = ("Name", "ID", "Favorite Pizza")

# Format our columns, *note: ttk creates a phantom column called (#0)
my_tree.column("#0", width=0, stretch=NO)  # this is the phantom column which we made invisible but can be made
# visible if you want
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favorite Pizza", anchor=W, width=140)

# Create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Customer Name", anchor=W)
my_tree.heading("ID", text="Id", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite pizza", anchor=W)

# this is when you want to automatically add from a database an example:

data = [["John", 1, "Pepper"],
        ["James", 2, "Onion"],
        ["Jake", 3, "Tomato"],
        ["Jonathan", 4, "Potato"],
        ["Jerald", 5, "Garlic"],
        ["Josh", 6, "Sauce"]]

count = 0
for record in data:
    my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2]))
    count += 1

# add data, this is for when you hard code it into the tree view
"""
my_tree.insert(parent="", index="end", iid=0, text="", values=("John", 1, "Pepper"))
my_tree.insert(parent="", index="end", iid=1, text="", values=("James", 2, "Onion"))
my_tree.insert(parent="", index="end", iid=2, text="", values=("Jake", 3, "Tomato"))
my_tree.insert(parent="", index="end", iid=3, text="", values=("Jonathan", 4, "Potato"))
my_tree.insert(parent="", index="end", iid=4, text="", values=("Jerald", 5, "Garlic"))
my_tree.insert(parent="", index="end", iid=5, text="", values=("Josh", 6, "Sauce"))
"""

# add child or sub column
"""
my_tree.insert(parent="", index="end", iid=6, text="Child", values=("Steve", 1.2, "Maggi"))
my_tree.move("6", "0", "0")
"""

# frame for layout of the software
# Labels
add_frame = Frame(app)
add_frame.pack(pady=20)

nL = Label(add_frame, text="Name")
nL.grid(row=0, column=0)

iL = Label(add_frame, text="ID")
iL.grid(row=0, column=1)

tL = Label(add_frame, text="Topping")
tL.grid(row=0, column=2)

# Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1, padx=20)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)


# Add record function, this is for getting data from the user and automatically adding it into the tree view database
def add():
    global count
    my_tree.insert(parent="", index="end", iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()))
    count += 1
    # clear the box
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


# remove all records
def remove_all():
    # this will get a list of all the columns in our record
    for record in my_tree.get_children():
        my_tree.delete(record)


# remove one selected
def remove_one():
    # check if something is selected in our tree view, putting [0] is for when you want the user to select only one,
    # if not you can remove it
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


# Select record
def select():
    # clear the selected data
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    # grab the number of the selected
    selected = my_tree.focus()

    # grab the selected number's values
    values = my_tree.item(selected, "values")

    # output to entry boxes
    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


# update record
def update():
    # grab selected record which are in numbers
    selected = my_tree.focus()

    # grab the selected number's values and save
    my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), topping_box.get()))

    # clear the selected data
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)
    update_record.destroy()


# binding click function
def clicker(e):
    global update_record
    select()
    update_record = Button(app, text="Update", command=update)
    update_record.pack(pady=10)


# Buttons
add_record = Button(app, text="Add record", command=add)
add_record.pack(pady=20)

remove_record = Button(app, text="Remove all records", command=remove_all)
remove_record.pack(pady=10)

remove_a_record = Button(app, text="Remove a record", command=remove_one)
remove_a_record.pack(pady=10)


# Bindings
# bind the balloon tipper at the top of the code as name tip
tip.bind_widget(remove_record, balloonmsg="Delete multiple records")
my_tree.bind("<Double-1>", clicker)  # <Double-1> is the binding for double clicking
app.mainloop()
