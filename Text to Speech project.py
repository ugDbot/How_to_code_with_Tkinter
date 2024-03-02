from tkinter import *
import pyttsx3

app =Tk()
app.title("Text to Speech")
app.geometry("400x400")

def talk():
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    voices= engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id) #to change voices of the textTospeech
    engine.say(my_Entry.get())

    engine.runAndWait()
    my_Entry.delete(0, END)



my_Entry = Entry(app)
my_Entry.pack(pady=10)

btn =Button(app, text="Speak", command=talk)
btn.pack(pady=10)



app.mainloop()