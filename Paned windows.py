from tkinter import *
from tkinter import ttk
app = Tk()
app.geometry("400x400")
app.title("Paned window")

#panels
panel_1 =PanedWindow(bd=4, relief="raised")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="Left panel")
panel_1.add(left_label)

panel_2 =PanedWindow(panel_1, orient= VERTICAL, bd=4, relief="raised")
panel_1.add(panel_2)

#creare a label in panel 2
right =Label(panel_2, text="Right panel")
panel_2.add(right)

#bottom = Label(panel_2, text="Bottom panel")
#panel_2.add(bottom)



app.mainloop()