from tkinter import *
from random import randint
import customtkinter

app = Tk()
app.title("Rock, paper, scissors")
app.geometry("500x400")
app.config(bg="white")


# reset
def reset_all():
    global img, img2, img3, selected
    cpu_ai.config(image=img)
    cpu_answer.config(text="")
    win_loose.config(text="...")
    win_loose.place(x=220, y=300)
    selected = ""


# define cpu functionality
def cpu_choice():
    global selected, img, img2, img3

    # prompt the cpu to choose a random number within the choices
    if selected:
        random_number = randint(0, 2)
        item = options[random_number]
        cpu_answer.config(text=item)
    else:
        return

    # define the different scenarios if the user picks rock, paper, scissors and what the computer should do
    while selected == "rock":
        if item == "rock":
            cpu_ai.config(image=img)
            win_loose.config(text="...")
            win_loose.place(x=220, y=300)
        elif item == "paper":
            cpu_ai.config(image=img3)
            win_loose.config(text="You Loose")
            win_loose.place(x=150, y=300)
        elif item == "scissors":
            cpu_ai.config(image=img2)
            win_loose.config(text="You Win!")
            win_loose.place(x=150, y=300)
        break

    while selected == "paper":
        if item == "rock":
            cpu_ai.config(image=img2)
            win_loose.config(text="You Win!")
            win_loose.place(x=150, y=300)
        elif item == "paper":
            cpu_ai.config(image=img)
            win_loose.config(text="...")
            win_loose.place(x=220, y=300)
        elif item == "scissors":
            cpu_ai.config(image=img3)
            win_loose.config(text="You Loose")
            win_loose.place(x=150, y=300)
        break

    while selected == "scissors":
        if item == "rock":
            cpu_ai.config(image=img3)
            win_loose.config(text="You Loose")
            win_loose.place(x=150, y=300)
        elif item == "paper":
            cpu_ai.config(image=img2)
            win_loose.config(text="You Win!")
            win_loose.place(x=150, y=300)
        elif item == "scissors":
            cpu_ai.config(image=img)
            win_loose.config(text="...")
            win_loose.place(x=220, y=300)
        break


# define user choices
def rock_picked():
    global selected
    selected = "rock"
    cpu_choice()


def paper_picked():
    global selected
    selected = "paper"
    cpu_choice()


def scissors_picked():
    global selected
    selected = "scissors"
    cpu_choice()


# create CPU options
options = ["rock", "paper", "scissors", ]

# create Buttons
rock = customtkinter.CTkButton(app, text="Rock", fg_color="white", hover_color="light grey", text_color="black",
                               command=rock_picked)
rock.place(x=10, y=100)

paper = customtkinter.CTkButton(app, text="Paper", fg_color="white", hover_color="light grey", text_color="black",
                                command=paper_picked)
paper.place(x=10, y=150)

scissors = customtkinter.CTkButton(app, text="Scissors", fg_color="white", hover_color="light grey", text_color="black",
                                   command=scissors_picked)
scissors.place(x=10, y=200)



# Create labels
global img, img2, img3
img = PhotoImage(file="C:/Users/admin/Pictures/AI.png")
img2 = PhotoImage(file="C:/Users/admin/Pictures/AI2.png")
img3 = PhotoImage(file="C:/Users/admin/Pictures/AI3.png")
cpu_ai = Label(app, image=img, bg="white")
cpu_ai.place(x=350, y=100)

cpu_answer = Label(app, text="", bg="white", font=("helvetica", 20))
cpu_answer.place(x=365, y=200)

vs_label = Label(app, text="VS", font=("helvetica", 20), bg="white")
vs_label.place(x=220, y=150)

win_loose = Label(app, text="...", font=("helvetica", 30), bg="white")
win_loose.place(x=220, y=300)

# create menus
my_menu = Menu(app)
app.config(menu=my_menu)
# Add buttons to menu----------
# reset
reset = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Menu", menu=reset)
reset.add_command(label="Reset", command=reset_all)

app.mainloop()
