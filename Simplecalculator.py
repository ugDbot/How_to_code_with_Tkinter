from tkinter import *


app = Tk()
app.title("Simple Calculator")
app.iconbitmap('C:/Users/admin/Pictures/icom.ico')


e = Entry(app, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def num_click(number):
    current =e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def but_clear():
    e.delete(0, END)

def but_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def but_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))

def but_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def but_multi():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def but_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)



#define buttons
button_1 = Button(app, text="1", padx=40, pady=20,command = lambda: num_click(1))
button_2 = Button(app, text="2", padx=40, pady=20,command = lambda: num_click(2))
button_3 = Button(app, text="3", padx=40, pady=20,command = lambda: num_click(3))
button_4 = Button(app, text="4", padx=40, pady=20,command = lambda: num_click(4))
button_5 = Button(app, text="5", padx=40, pady=20,command = lambda: num_click(5))
button_6 = Button(app, text="6", padx=40, pady=20,command = lambda: num_click(6))
button_7 = Button(app, text="7", padx=40, pady=20,command = lambda: num_click(7))
button_8 = Button(app, text="8", padx=40, pady=20,command = lambda: num_click(8))
button_9 = Button(app, text="9", padx=40, pady=20,command = lambda: num_click(9))
button_0 = Button(app, text="0", padx=40, pady=20,command = lambda: num_click(0))

button_equal = Button(app, text="=", padx=88, pady=20,command = but_equal)
button_clear = Button(app, text="Clear", padx=78, pady=20,command = but_clear)

button_add = Button(app, text="+", padx=40, pady=20,command = but_add)
button_sub = Button(app, text="-", padx=40, pady=20,command = but_add)
button_multiply = Button(app, text="*", padx=40, pady=20,command = but_add)
button_div = Button(app, text="/", padx=40, pady=20,command = but_add)

button_quit = Button(app, text="Exit", command = app.quit, padx=10, pady=10)
button_quit.grid(row=7, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=3)

button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_div.grid(row=6, column=0)










app.mainloop()