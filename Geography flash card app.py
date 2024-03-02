from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk,Image
from random import randint

app = Tk()
app.title("Special character")
app.geometry("500x550")

#randomizing states
def rando_states():
    global randovar
    # create states name list
    our_states = ["abia", "adamawa", "akwa ibom", "anambra", "bauchi", "bayelsa", "benue", "borno", "cross river",
                  "delta",
                  "ebonyi", "edo", "ekiti", "enugu", "gombe", "imo", "jigawa", "kaduna",
                  "kano", "katsina", "kebbi", "kogi", "kwara", "lagos", "nasarawa", "niger", "ogun", "ondo", "osun",
                  "oyo", "plateau", "rivers", "sokoto", "taraba", "yobe", "zamfara"]

    # generate a random number and assign it to your states to generate random states
    rando = randint(0, len(our_states) - 1)
    randostate = "C:/Users/admin/Desktop/Nigerian states/" + our_states[rando] + ".png"
    randovar = our_states[rando]

    # create state images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(randostate))
    show_state.configure(image= state_img)




#create answer function
def state_answer():
    #create a logic that replace spaces and joins them together and makes sure it's all in lower case
    answer = answer_entry.get()
    answer2 = answer.replace(" ", "")

    #check if answers are right or correct
    if answer2.lower() == randovar:
        response = "Correct!" + " " + randovar.title()#title() makes the first letter capital
    else:
        response = "Incorrect!" + " " + randovar.title()

    answer_lbl.configure(text=response)
    rando_states()
    answer_entry.delete(0, END)




#State flashcard function
def states():
    global show_state

    global answer_entry
    global answer_lbl
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    my_lbl = Label(state_frame, text="States").pack()

    #label to create the states frame then call the rando_states()
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    rando_states()



    #entry box to put right answers
    answer_entry = Entry(state_frame, font=("Courier, 10"))
    answer_entry.pack(pady=15)

    # create button to randomize state images
    rando_button = Button(state_frame, text="Next state", command=states)
    rando_button.pack(pady=10)

    #create button to answer questions
    answer_button = Button(state_frame, text="Answer", command=state_answer)
    answer_button.pack(pady=5)

    #label to show if we are right or not
    answer_lbl = Label(state_frame, text=" ", font=("Courier, 18"))
    answer_lbl.pack(pady=15)






#State capital flash card function
def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)


#function to hide previous frame
def hide_all_frames():
    #loop to know all the widgets in the program and hide them
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    #to forget the frames
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


#create our menu
my_menu =Menu(app)
app.configure(menu=my_menu)

#create Geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label = "States Capital", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="exit", command=app.quit)


#create frames
state_frame = Frame(app, width=500, height=500)
state_capitals_frame = Frame(app, width=500, height=500)


app.mainloop()