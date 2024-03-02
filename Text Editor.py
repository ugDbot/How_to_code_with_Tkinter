from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api

app = Tk()
app.title("Text Boxes")
app.geometry("1200x680")

# Read only r
# Read and Write r+ (beginning of file)
# Write Only w (over_written)
# Write and Read w+ (over written)
# Append Only a (end of file)
# Append and Read a+ (end of file)


# ====================================BASICS OF TEXT BOXES============================================================
"""
#define clear functions
def clear():
    my_text.delete(1.0, END)

#grab the text from the text box
def get_text():
    my_label.config(text=my_text.get(1.0, END))

# Open files
def open_text():
    global text_file
    text_file = filedialog.askopenfilename(initialdir = "C:/Users/admin/PycharmProjects/", title="Open Text files", filetypes=(("Text Files", "*.txt"),))
    name = text_file
    name = name.replace("C:/Users/admin/PycharmProjects/", "")
    name = name.replace(".txt", "")
    open_text_file = open(text_file, "r")
    stuff = open_text_file.read()
    my_text.insert(END, stuff)
    open_text_file.close()
    app.title(f"{name} - Textpad")

#save file
def save_txt():
    global text_file
    text_file = open(text_file, "w")
    text_file.write(my_text.get(1.0, END))

#add image
def add_img():
    global my_img
    my_img = PhotoImage(file="C:/Users/admin/PycharmProjects/Mummy's planner GUI project/plans_image/login_img2.png")
    # GET THE CURRENT CURSOR POSITION
    position = my_text.index(INSERT)
    my_text.image_create(END, image=my_img)

# select a text that we have highlighted
def select():
    selected = my_text.selection_get()
    my_label.config(text = selected)

# make a text bold
def bolder():
    # create a bold font tag
    bold_font = font.Font(my_text, my_text.cget("font"))

    # configure the bold tag
    bold_font.configure(weight = "bold")
    my_text.tag_configure("bold", font=bold_font)

    # check if the text is already bold or not
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

# make a text italics
def Its():
    # create a italic font tag
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # configure the italic tag
    my_text.tag_configure("italic", font=italics_font)

    # check if the text is already italic or not
    current_tags = my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")




scroll_frame = Frame(app)
scroll_frame.pack(pady=20)

# create scroll bar
text_scroll = Scrollbar(scroll_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(scroll_frame, width=60, height=20, selectbackground = "yellow", selectforeground = "black",yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# configure our scrollbar
text_scroll.config(command=my_text.yview)

button_frame = Frame(app)
button_frame.pack()


clear_btn = Button(button_frame, text="Clear screen", command=clear)
clear_btn.grid(row=0, column=0)

get_btn = Button(button_frame, text="Get Text", command=get_text)
get_btn.grid(row=0, column=1, padx=20)

open_btn = Button(button_frame, text="open text files", command=open_text)
open_btn.grid(row=1, column=0)

save_btn = Button(button_frame, text="Save File", command=save_txt)
save_btn.grid(row=1, column=1, pady=20)

image_btn = Button(button_frame, text="Add Image", command=add_img)
image_btn.grid(row=1, column=3)

select_btn = Button(button_frame, text="Select", command=select)
select_btn.grid(row=0, column=3)

bold_btn = Button(button_frame, text = "Bold", command= bolder)
bold_btn.grid(row=2, column=0)

italics_btn = Button(button_frame, text="Italics", command=Its)
italics_btn.grid(row=2, column=1)

redo_btn = Button(button_frame, text="Redo", command=my_text.edit_redo)
redo_btn.grid(row=2, column=3)

undo_btn = Button(button_frame, text="Undo", command=my_text.edit_undo)
undo_btn.grid(row=3, column=0)

my_label = Label(app, text="")
my_label.pack(pady=20)
"""

# ===================================CREATE A STANDARD TEXT EDITOR=============================================================


# Global variables--------------------------
# create current file open variable
global current_status_name
current_status_name = False

# create highlighted text variable
global selected
selected = False


# create New file function
def new_file():
    my_text.delete("1.0", END)
    app.title("New File - Textpad")
    status_bar.config(text="        New File")

    # reset the current file variable
    global current_status_name
    current_status_name = False


# create Open file function
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="C:/Users/admin/Desktop/", title="Open file", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    # check to see if the file has a name and make global to be used elsewhere
    if text_file:
        global current_status_name
        current_status_name = text_file

    name = text_file

    # Update title an status bar
    status_bar.config(text=f"        {name}")
    name_title = name.replace("C:/Users/admin/Desktop/", "")
    app.title(f"{name_title} - Textpad")

    # Open file
    text_file_open = open(text_file, "r")
    stuff = text_file_open.read()

    # add file to text box
    my_text.insert(END, stuff)

    # Close file
    text_file_open.close()


# Save as file function
def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/admin/Desktop/",
                                             title="Save File", filetypes=(
            ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # update status and title bar
        name = text_file
        status_bar.config(text=f"        Saved: {name}")
        name_title = name.replace("C:/Users/admin/Desktop/", "")
        app.title(f"{name_title} - Textpad")

        # save file
        text_file_save = open(text_file, "w")
        text_file_save.write(my_text.get(1.0, END))

        # close the file
        text_file_save.close()


# save file function
def save_file():
    global current_status_name
    # check if the file exists
    if current_status_name:
        # save file
        text_file_save = open(current_status_name, "w")
        text_file_save.write(my_text.get(1.0, END))
        # close the file
        text_file_save.close()
        # update the status
        status_bar.config(text=f"        Saved: {current_status_name}")
    else:
        save_as()


# define cut function
def cut_text(e):
    global selected
    # check to see if we used Keyboard shortcut and access the windows clipboard in memory and assign to a variable
    if e:
        selected = app.clipboard_get()
    else:
        # check if a text is highlighted
        if my_text.selection_get():
            # grab the highlighted text and save it
            selected = my_text.selection_get()

            # Delete highlighted text cus it has been cut
            my_text.delete("sel.first", "sel.last")
            # if we use the menu buttons make sure to clear the memory clipboard and append what's currently selected
            app.clipboard_clear()
            app.clipboard_append(selected)


# define copy function
def copy_text(e):
    global selected
    # check to see if we used Keyboard shortcut and access the windows clipboard in memory and assign to a variable
    if e:
        selected = app.clipboard_get()
    # check if a text is highlighted
    if my_text.selection_get():
        # grab the highlighted text and save it
        selected = my_text.selection_get()
        # if we use the menu buttons make sure to clear the memory clipboard and append what's currently selected
        app.clipboard_clear()
        app.clipboard_append(selected)


# define paste function
def paste_text(e):
    global selected
    # check to see if we used Keyboard shortcut and access the windows clipboard in memory and assign to a variable
    if e:
        selected = app.clipboard_get()
    else:
        # check if it was highlighted and cut
        if selected:
            # get the position of the cursor
            position = my_text.index(INSERT)
            # insert it in
            my_text.insert(position, selected)


# bold function
def bold_it():
    # create a bold font tag
    bold_font = font.Font(my_text, my_text.cget("font"))

    # configure the bold tag
    bold_font.configure(weight="bold")
    my_text.tag_configure("bold", font=bold_font)

    # check if the text is already bold or not
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


# italics function
def italics_it():
    # create a italic font tag
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # configure the italic tag
    my_text.tag_configure("italic", font=italics_font)

    # check if the text is already italic or not
    current_tags = my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


# change highlighted text color
def text_color():
    # pick a color and put [] to return the hex color code
    my_color = colorchooser.askcolor()[1]
    if my_color:
        # create a color font tag
        color_font = font.Font(my_text, my_text.cget("font"))

        # configure the color tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # check if the text is already colored or not
        current_tags = my_text.tag_names("sel.first")
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")


# change background color
def bg_color():
    # pick a color and put [] to return the hex color code
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)


# change all text color
def all_text_color():
    # pick a color and put [] to return the hex color code
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# Pint file function
def print_file():
    """
    # this gets the connected printer to your system
    printer_name = win32print.GetDefaultPrinter()
    status_bar.config(text=printer_name)
    """

    # grab file name
    file_to_print = filedialog.askopenfilename(initialdir="C:/Users/admin/Desktop/", title="Open file", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


# toolbar frame
toolbar_frame = Frame(app)
toolbar_frame.pack(fill=X)

# create main frame
my_frame = Frame(app)
my_frame.pack(pady=5)

# create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# horizontal scrollbar
hor_scroll = Scrollbar(my_frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)

# create a text widget
my_text = Text(my_frame, width=1100, height=39, font=("Helvetica", 10), selectbackground="Yellow",
               selectforeground="black", undo=True,
               yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# configure our scrollbar
text_scroll.configure(command=my_text.yview)

# configure our hor scrollbar
hor_scroll.configure(command=my_text.xview)

# create Menu
my_menu = Menu(app)
app.config(menu=my_menu)

# Add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste        ", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo        ", command=my_text.edit_redo, accelerator="(Ctrl+y)")

# Add color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# Add a status bar
status_bar = Label(app, text="        Ready", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# create edit binding
app.bind("<Control-Key-x>", cut_text)
app.bind("<Control-Key-c>", copy_text)
app.bind("<Control-Key-v>", paste_text)

# create buttons

# bold button
bold_btn = Button(toolbar_frame, text="Bold", command=bold_it)
bold_btn.grid(row=0, column=0, sticky=W, padx=5)

# italics button
italics_btn = Button(toolbar_frame, text="Italics", command=italics_it)
italics_btn.grid(row=0, column=1, padx=5)

app.mainloop()
