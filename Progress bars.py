from tkinter import *
from tkinter import ttk
import time

app = Tk()
app.title("Progress bar")
app.geometry("400x400")

def step():
    #progress_bar["value"] += 20
    #progress_bar.start(10)
    for x in range(5):
        progress_bar["value"] += 20
        app.update_idletasks() #allow things to update then show the task
        time.sleep(0.5)




def stop():
    progress_bar.stop()

progress_bar = ttk.Progressbar(app, orient=HORIZONTAL, length=1500, mode="determinate") #mode can be determinate or indeterminate
progress_bar.pack(pady=20)

btn = Button(app, text="Progress", command=step)
btn.pack(pady=20)

btn_2= Button(app, text="Stop", command=stop)
btn_2.pack(pady=20)

app.mainloop()