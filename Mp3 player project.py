from tkinter import *
import pygame #we use pygame to put songs cus it's more covenient
from tkinter import filedialog
import os
import time
from mutagen.mp3 import MP3 #we use this to check the duration of a song
import tkinter.ttk as ttk


app = Tk()
app.title("Mp3")
app.geometry("400x400")

pygame.mixer.init()


#a basic music player===================================================================
"""
def song():
    pygame.mixer.music.load("C:/Users/admin/Music/DojaCat.mp3")
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()

my_btn = Button(app, text= "Play song", command=song)
my_btn.pack(pady=20)

stop_btn = Button(app, text="Stop", command = stop)
stop_btn.pack(pady=20)
"""
#=========================================================================================



#THE MP3 PLAYER========================================================================================================================================
def add_song():
    song = filedialog.askopenfilename(initialdir="C:/Users/admin/Music/", title="Choose a song", filetypes= (("mp3 Files", "*.mp3"),))
    # remove the extensions from the song name
    song = song.replace("C:/Users/admin/Music/", "")
    song = song.replace(".mp3", "")
    # add song to list box
    song_box.insert(END, song)

def add_many_songs():
    song = filedialog.askopenfilenames(initialdir="C:/Users/admin/Music/", title="Choose a song",
                                      filetypes=(("mp3 Files", "*.mp3"),))
   # loop through the song list and replace the dir
    for song in song:
        # remove the extensions from the song name
        song = song.replace("C:/Users/admin/Music/", "")
        song = song.replace(".mp3", "")
        # add song to list box
        song_box.insert(END, song)
global stopped
stopped = False
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar_lbl.config(text = "")
    my_slider.config(value=0)
    global stopped
    stopped =True

def status_bar():
    # check for double timing
    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000
    slider_lbl.config(text = f"Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}")

    # convert it to time format
    converted_current_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
    status_bar_lbl.config(text=converted_current_time)

    # get the current song number cus this function returns the selection number

    next_one = song_box.curselection()

    # get song title from playlist
    song = song_box.get(ACTIVE)
    song = f"C:/Users/admin/Music/{song}.mp3"

    # get the duration with mutagen
    song_mut = MP3(song)

    # Get song length
    global song_length
    song_length =song_mut.info.length

    #convert to time format
    converted_song_length = time.strftime("%H:%M:%S", time.gmtime( song_length))

    #increase current time by 1 second
    current_time += 1
    if int(my_slider.get()) == int(song_length):
        status_bar_lbl.config(text=f"Time Elapsed: {converted_song_length}  of  {converted_song_length} ")
    elif paused:
        pass

    elif int(my_slider.get()) == int(current_time):
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))

        #convert to time format
        converted_current_time = time.strftime("%H:%M:%S", time.gmtime(int(my_slider.get())))

        #output time to status bar
        status_bar_lbl.config(text=f"Time Elapsed: {converted_current_time}  of  {converted_song_length} ")

        #move this along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)




    #=========status_bar_lbl.config(text=f"Time Elapsed: {converted_current_time}  of  {converted_song_length} ")
    #update slider pos value to current song pos
    #my_slider.config(value=int(current_time))



    status_bar_lbl.after(1000, status_bar)

def play():
    #set to false so song can play
    global stopped
    stopped = False

    song = song_box.get(ACTIVE)
    song = f"C:/Users/admin/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # call the status bar
    status_bar()
    #update slider to position


global paused #create global pauser variable
paused = False

def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    #reset the status
    status_bar_lbl.config(text="")
    my_slider.config(value=0)

    # get the current song number cus this function returns the selection number
    next_one = song_box.curselection()
    # add one to the current song
    next_one = next_one[0]+1
    # get song title from playlist
    song = song_box.get(next_one)
    song = f"C:/Users/admin/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # update the selection bar
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

def previous_song():
    # reset the status
    status_bar_lbl.config(text="")
    my_slider.config(value=0)

    # get the current song number cus this function returns the selection number
    next_one = song_box.curselection()
    # add one to the current song
    next_one = next_one[0] - 1
    # get song title from playlist
    song = song_box.get(next_one)
    song = f"C:/Users/admin/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # update the selection bar
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

def deleted_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def deleted_all_song():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()

def slide(x):
    #slider_lbl.config(text = f"{int(my_slider.get())}  of  {int(song_length)}")
    song = song_box.get(ACTIVE)
    song = f"C:/Users/admin/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))





# create playlist box
song_box = Listbox(app, bg = "black", fg = "green", width = 60, selectbackground = "grey", selectforeground = "white")
song_box.pack(pady=20)
#automatically add the songs from a path set which by default is music
song = os.listdir("C:/Users/admin/Music/")
for song in song:
    # remove the extensions from the song name
    song = song.replace("C:/Users/admin/Music/", "")
    song = song.replace(".mp3", "")
    # add song to list box
    song_box.insert(END, song)

# create button frames
control_frame = Frame(app)
control_frame.pack()

# create buttons
back_btn = Button(control_frame, text="back", command = previous_song)
forward_btn = Button(control_frame, text="forward", command = next_song)
play_btn = Button(control_frame, text="play", command=play)
pause_btn = Button(control_frame, text="pause", command=lambda: pause(paused))
stop_btn = Button(control_frame, text="stop", command=stop)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# create menu
my_menu = Menu(app)
app.config(menu=my_menu)

# Add buttons to menu----------
# add a song
add_songs = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=add_songs)
add_songs.add_command(label="Add a song", command=add_song)
# add many songs
add_songs.add_command(label="Add many songs", command=add_many_songs)
# delete a song
delete_songs = Menu(my_menu)
my_menu.add_cascade(label="Delete songs", menu=delete_songs)
delete_songs.add_command(label="Delete song", command=deleted_song)
delete_songs.add_command(label="Delete all song", command=deleted_all_song)

#status bar
status_bar_lbl = Label(app, text="", bd=1, relief=GROOVE, anchor=E)
status_bar_lbl.pack(fill=X, side=BOTTOM, ipady=2)

#Create music slider
my_slider = ttk.Scale(app, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=20)

#create temporary slider label
slider_lbl = Label(app, text="0")
slider_lbl.pack(pady=20)



app.mainloop()