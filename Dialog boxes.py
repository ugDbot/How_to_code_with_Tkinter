from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

app = Tk()
app.title("Open files with dialog boxes")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")
def open():
    global my_img
    app.filename = filedialog.askopenfilename(initialdir="C:/Users/admin/Desktop/pythonimg", title="Select a file",
                                              filetypes=(("jpg files", "*.jpg*"), ("all files", "*.*")))
    my_img = ImageTk.PhotoImage(Image.open(app.filename))
    img_lbl = Label(app, image=my_img).pack()


btn = Button(app, text="open file", command=open).pack()




app.mainloop()