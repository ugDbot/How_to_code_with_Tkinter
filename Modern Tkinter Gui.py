from tkinter import *
import customtkinter
import sys

customtkinter.set_appearance_mode("System")# Modes: system(default), light, dark
customtkinter.set_default_color_theme("dark-blue") #themes: blue (default), dark-blue, green

app = customtkinter.CTk()
#Label frame
lblframe = customtkinter.CTkFrame(app, corner_radius=10)
lblframe.pack(pady =10)

#button
button = customtkinter.CTkButton(app, text="hello")
button.pack()

#entry box
entry = customtkinter.CTkEntry(lblframe, width=400, height=40, border_width = 1, #to set a default text on the entry:
                                placeholder_text="Enter a word", text_color="silver", text_font="Courier")
entry.pack()
#Custom Tkinter doesnt have a text box widget so we hack around it with a frame and a tkinter text box
text_frame = customtkinter.CTkFrame(app, corner_radius=10)
text_frame.pack(pady=10)

text_box = Text(text_frame, height=20, width=67, wrap=WORD, bd=0, bg="#292929", fg="silver")
text_box.pack(pady=10, padx=10)






app.mainloop()