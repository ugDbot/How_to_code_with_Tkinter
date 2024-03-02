from tkinter import *
from PIL import ImageTk,Image

app =Tk()
app.title("Image viewer")
app.iconbitmap('C:/Users/admin/Pictures/company.ico')


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("C:/Users/admin/Desktop/pythonimg/img7.jpg"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

status = Label(app, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])
    button_forward = Button(app, text=">>", command=lambda: forward(img_num+1))
    button_back = Button(app, text="<<", command=lambda: back(img_num-1))

    if img_num == 7:
        button_forward = Button(app, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
#update status bar
    status = Label(app, text="Image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)




def back(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num - 1])
    button_forward = Button(app, text=">>", command=lambda: forward(img_num + 1))
    button_back = Button(app, text="<<", command=lambda: back(img_num - 1))

    if img_num == 1:
        button_back = Button(app, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
#update status bar
    status = Label(app, text="Image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



but_back = Button(app, text="<<", command = back, state=DISABLED)
but_exit = Button(app, text="exit", command = app.quit)
but_forw = Button(app, text=">>", command = lambda: forward(2))

but_back.grid(row=1, column=0)
but_exit.grid(row=1, column=1)
but_forw.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)












app.mainloop()