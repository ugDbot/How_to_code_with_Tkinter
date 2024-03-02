from tkinter import *

app = Tk()
app.title("Search")
app.geometry("400x400")


# Update the list box
def update(data):
    # Clear the listbox
    list.delete(0, END)

    # Add toppings -  it's called data cus we passed food as data in the update function
    for item in data:
        list.insert(END, item)


# update entry box when list is clicked
def fillout(e):
    entry.delete(0, END)

    # A dd selected item to the entry
    listed = list.get(ANCHOR)
    entry.insert(0, listed)


# Function to check if the entry has been clicked and checking if its in the list
def check(e):
    # grab what was typed
    typed = entry.get()

    if typed == " ":
        data = food
    else:
        data = []
        for item in food:
            if typed.lower() in item.lower():  # the lower() is to make sure it's not case sensitive
                data.append(item)
    # update listbox with selected item
    update(data)


label = Label(app, text="Type", font=("Helvetica", 14), fg="grey")
label.pack(pady=20)

# Create entry box
entry = Entry(app, font=("Helvetica", 20))
entry.pack()

# Create a listbox
list = Listbox(app, width=50)
list.pack(pady=40)

# Create a list of food
food = ["Pepper", "Papaye", "Onions", "okpa", "salt", "semo", "eba", "egg", "yolk", "fufu", "fried rice", "jollof rice"]

# Add to the list
update(food)

# Bindings
list.bind("<<ListboxSelect>>", fillout)
entry.bind("<KeyRelease>", check)
app.mainloop()
