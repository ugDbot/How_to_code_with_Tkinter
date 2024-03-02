from tkinter import *
import time

app=Tk()
app.title("Timers")
app.geometry("400x400")

#how to make your program wait or delay
def update():
    lbl.config(text="New text")
lbl = Label(app, text="Old text")
lbl.pack(pady=20)
lbl.after(5000, update) #the seocnds is in milliseconds...1000 millisecond = 1 second




#create clock woth tkinter
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    time_lbl.configure(text = hour + ":" + minute + ":" + second)
    day_lbl.configure(text=day)
    time_lbl.after(1000, clock)


time_lbl = Label(app, text = "", font=("Courier, 48"), bg="black" ,fg="green")
time_lbl.pack(pady=20)

day_lbl = Label(app, text="", font=("Courier, 20"))
day_lbl.pack(pady=20)



clock()
app.mainloop()