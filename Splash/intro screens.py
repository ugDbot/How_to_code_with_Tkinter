from tkinter import *

splash_root = Tk()
splash_root.title("")
splash_root.geometry("400x200")
# hide titlebar
splash_root.overrideredirect(True)

splash_label = Label(splash_root, text="Intro!!", font=("helvetica", 30))
splash_label.pack(pady=10)


def mainwindow():
    splash_root.destroy()
    app = Tk()
    app.title("Opened")
    app.geometry("400x600")


# splash screen timer
splash_root.after(3000, mainwindow)

mainloop()
