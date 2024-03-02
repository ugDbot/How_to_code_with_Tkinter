from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

app = Tk()
app.title("Weather app")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")
app.geometry("400x200")

def graph():
    house_price = np.random.normal(200000, 25000, 5000)
    plt.hist(house_price, 50)
    plt.show()

btn = Button(app, text="Graph", command=graph).pack()


app.mainloop()