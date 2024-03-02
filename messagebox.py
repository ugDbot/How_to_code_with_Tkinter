from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

app = Tk()
app.title("Message Box")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")


#types of popup:  showinfo,  showwarning,  showerror,  askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is the popup!", "Hello World")
    #Label(app, text=response)
    if response == 1:
        Label(app, text="You clicked yes").pack()
    else:
        Label(app, text="You clicked no").pack()


Button(app, text="Popup", command=popup).pack()






app.mainloop()