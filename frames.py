from tkinter import *
from PIL import ImageTk,Image

app = Tk()
app.title = "Frames"
app.iconbitmap('C:/Users/admin/Pictures/company.ico')

frame = LabelFrame(app, text="this is my frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="okay")
b.pack()








app.mainloop()