from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Combo and ListBoxes")
app.geometry("500x500")

# Creating list
sizes = ["Small",
         "Medium",
         "Large"]

small_colors = ["Red",
                "Green",
                "Blue",
                "Black"]

meduim_colors = ["Red",
                 "Green"]

large_colors = ["Blue",
                "Black"]
# functions for the binding
def pick_color(e):
    # sets the other combo box according to what was selected
    if my_combo.get() == "Small":
        color_combo.config(value=small_colors)
    if my_combo.get() == "Medium":
        color_combo.config(value=meduim_colors)
    if my_combo.get() == "Large":
        color_combo.config(value=large_colors)

def list_color(e):
    my_list2.delete(0, END)
    if my_list1.get(ANCHOR) == "Small":
        for item in small_colors:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Medium":
        for item in meduim_colors:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Large":
        for item in large_colors:
            my_list2.insert(END, item)



# create a drop down box
my_combo = ttk.Combobox(app, value=sizes)
# my_combo.current(0) - this line  can be used to set the default text to the first item in the list
my_combo.insert(0, "Shirt Sizes")
my_combo.pack(pady=20)

color_combo = ttk.Combobox(app, value=[" "])
color_combo.insert(0, "Available Shirt Colors")
color_combo.pack(pady=20)

# bind combo box so we can select something from the combo box and have it do something
my_combo.bind("<<ComboboxSelected>>", pick_color)

# List Box
my_frame = Frame(app)
my_frame.pack(pady=50)

my_list1 = Listbox(my_frame)
my_list2 = Listbox(my_frame)
my_list1.grid(row=0, column=0)
my_list2.grid(row=0, column=1, padx=20)

# add items to list1
for item in sizes:
    my_list1.insert(END, item)

# bind listbox
my_list1.bind("<<ListboxSelect>>", list_color)


app.mainloop()