from tkinter import *
import customtkinter

app = Tk()
app.title("Login")
app.geometry("400x500")

bg = PhotoImage(file = "C:/Users/admin/Pictures/login sample.png")

# Define canvas
my_canvas = Canvas(app, width=400, height=500, bd=0, highlightthickness = 0)
my_canvas.pack(fill="both", expand=True)

# Put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor=NW)

# Entries
un_entry = customtkinter.CTkEntry(app, text_font=("Helvetica", 24), width=250, placeholder_text="username",
                                  fg_color="white", border_color="white", border_width=0, text_color="black")
pw_entry = customtkinter.CTkEntry(app, text_font=("Helvetica", 24), width=250,  placeholder_text="password",
                                  fg_color="white", border_color="white", border_width=0, text_color="black")

# code to show stars for privacy in the password entry
pw_entry.configure(show="*")


#add entry boxes to canvas
un_window = my_canvas.create_window(60, 290, anchor="nw", window=un_entry)
pw_window = my_canvas.create_window(60, 370, anchor="nw", window=pw_entry)

# Login Button
lg_btn = customtkinter.CTkButton(app, text="Login", fg_color = "white", hover_color="light grey", text_color="black", width=250)
lg_btn_window = my_canvas.create_window(60, 450, anchor="nw", window=lg_btn)



app.mainloop()