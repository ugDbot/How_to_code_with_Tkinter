from tkinter import *
from tkcalendar import *

app = Tk()
app.title("Codemy.com")
app.geometry("600x400")

cal = Calendar(app, selectmode="day", year=2022, month=8, day=28)
cal.pack(pady=20, fill="both", expand=True)

def grab_date():
    my_label.config(text="The date is:  " + cal.get_date())

my_button = Button(app, text="Get date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(app,text="")
my_label.pack(pady=20)


app.mainloop()