import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import requests
import sys
import json
import sqlite3
from tkinter import ttk
import codecs
from itertools import groupby
from tkcalendar import *
from datetime import date



customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("Login page")
app.geometry("400x600")
app.resizable(False, False)



#==========================define table========================================
def submit():
    global input_username

    # add sqlite3 function=====================
    users = sqlite3.connect("users.db")
    db = users.cursor()
    #create table========================
    db.execute("CREATE TABLE IF NOT EXISTS usernames(user_name text)")
    users.commit()

    #authentification=======================================
    data = db.execute("SELECT user_name FROM usernames").fetchall()
    result = []
    #loop to add a new user name if it doesn`t exist========================
    for t in data:
        result.append(t[0])
    input_username= login_entry.get()

    #function to check if the username exist else it will add=======================
    # function to check if the username exist else it will add=======================
    if input_username in result:
        # clear textbox after submittion and open second window=======================
        login_entry.delete(0, END)
        app.withdraw()
        planningboard()

        users.close()

    elif input_username == " " or "":
        messagebox.showerror("Oh no!", "Incorrect login attributes, Put down a name")
    # check if the entry box is empty=====
    elif len(input_username) == 0:
        messagebox.showerror("Oh no!", "Incorrect login attributes, Put down a name")




    # if the user does not exist, add him and create his/her table
    else:
        try:
            db = users.cursor()
            db.execute("INSERT INTO usernames (user_name) VALUES (:u_name)",
                       {"u_name": login_entry.get()
                        })
            users.commit()
            users.close()
            # add sqlite3 function
            plans = sqlite3.connect("planning.db")
            db = plans.cursor()
            # create table new table for user we use the {} as an instance placeholder to create unique tables===========================================
            db.execute("CREATE TABLE {} (plans text, "
                                        "pending text, "
                                        "done text)".format(input_username))

            plans.commit()
            plans.close()
            messagebox.showinfo("Welcome", "Welcome" + " " + input_username)
            app.withdraw()
            planningboard()
        except Exception as error:
            messagebox.showerror("Oh no!", "Name format is not allowed, No spacing before, between or after writing the username and no use of numbers. Try again")


#=========================================create the planning board======================================
def planningboard():
        global shows_p
        global plans_list
        global print_records
        app2 = customtkinter.CTkToplevel()
        app2.title("mummy's planner")
        app2.geometry("1050x400")
        app2.resizable(False, False)
        plans = sqlite3.connect("planning.db")
        recent_table = plans.cursor()




        #===============================create add button=====================================
        def add():
            try:
                plans = sqlite3.connect("planning.db")
                db = plans.cursor()



                insert_list = db.execute("INSERT INTO {} (plans) VALUES (:plan)".format(input_username),
                                         {"plan": planning_entry.get(1.0, "end-1c") + "  " + cal.get_date()
                                          })
                result = []

                # loop to add a new plan
                for t in insert_list:
                    result.append(t[0])
                plans.commit()
                messagebox.showinfo("Success", "The Plan has been added and updated")
            except Exception as a:
                messagebox.showerror("Oh no!", "There was an issue with updating the database, Try again")
#--------------------------------------------------------------------------------------------------------------------------------






        #=========================================create reset button=================================
        def reset():
            try:
                plans = sqlite3.connect("planning.db")
                db = plans.cursor()

                db.execute("DELETE FROM {}".format(input_username))
                plans.commit()
                plans.close()
                planning_entry.delete("1.0" ,"end")
                messagebox.showinfo("Success", "Database has been reset successfully")
            except Exception as e:
                messagebox.showerror("Oh no!", "Database reset wasn't succesfull, Try again")
#--------------------------------------------------------------------------------------------------------------------------


        def logout():
            app2.withdraw()
            app.deiconify()

#-------------------------------------------------------------------------------------------------------------------------

        def pendingapp():
            app2.withdraw()
            appPend = customtkinter.CTkToplevel()
            appPend.title("mummy's planner")
            appPend.geometry("900x600")
            plans = sqlite3.connect("planning.db")
            recent_table = plans.cursor()
            show_pend = recent_table.execute("SELECT oid, pending FROM {} WHERE pending IS NOT NULL".format(input_username))
            shows_P = show_pend.fetchall()
            print_pend_rows_with_data = ""
            for record in shows_P:
                print_pend_rows_with_data += str(record[0]) + " " + str(record[1]) + " " + "\n"
            plans.commit()
#-----------------------------------------------------------------------------------------------------------------------------
            def addtodone():
                info = pend_entry.get()
                try:
                    plans = sqlite3.connect("planning.db")
                    id = plans.cursor()
                    search = id.execute("SELECT pending FROM {} WHERE oid = {}".format(input_username, info))
                    inserter = search.fetchall()
                    inserting = ""
                    for insertValue in inserter:
                        inserting = str(insertValue[0])
                    insert_list = id.execute(
                        "UPDATE {} SET done = :donE WHERE oid = {}".format(input_username, info),
                        {"donE": inserting,
                         })
                    result = []

                    # loop to add a new plan
                    for t in insert_list:
                        result.append(t)
                    plans.commit()

                    insert_list2 = id.execute(
                        "UPDATE {} SET pending = :donepend WHERE oid = {}".format(input_username, info),
                        {"donepend": inserting + " (done)",
                         })
                    result = []

                    # loop to add a new plan
                    for r in insert_list2:
                        result.append(r)
                    plans.commit()
                    messagebox.showinfo("success", "The plan has been added to Finished plans")

                except Exception as p:
                    messagebox.showerror("Oh no!", "The plan wasn't added, Try again")
#------------------------------------------------------------------------------------------------------------------------
            def backpend():
                appPend.withdraw()
                app2.deiconify()
#-------------------------------------------------------------------------------------------------------------------------
            # ====================add scrollers=====================
            # create main frame
            main_frame = Frame(appPend, bg="#292929")
            main_frame.pack(fill=BOTH, expand=1)

            # create a canvas
            my_canvas = Canvas(main_frame, bg="#292929")
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            # add scrollbar to the canvas
            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # configure the canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            # create another frame inside the canvas
            second_framePend = Frame(my_canvas, bg="#292929")

            # add that new frame to a window in the canvas
            my_canvas.create_window((0, 0), window=second_framePend, anchor="nw")
#-------------------------------------------------------------------------------------------------------------------------
            # ===============================create pending widget===============================
            pend_lbl = customtkinter.CTkLabel(second_framePend, text="Pending plans", text_font=("Courier, 30"))
            pend_lbl.grid(row=0, column=0, pady=1, padx=1)

            user_id_pend_label = customtkinter.CTkLabel(second_framePend, text="User: " + str(input_username),
                                                         text_font=("Courier, 10"))
            user_id_pend_label.grid(row=1, column=0, padx=1, pady=1)

            pend_entry = customtkinter.CTkEntry(second_framePend, border_width=2,
                                                 placeholder_text="What number is the plan?",
                                                 corner_radius=6, width=250)
            pend_entry.grid(row=2, column=0, padx=5, pady=5)

            pend_addtodone_btn = customtkinter.CTkButton(second_framePend, text="Add to finished plans",
                                                             fg_color="black", hover_color="dark grey", border_width=2,
                                                             corner_radius=6,
                                                             border_color="black", command=addtodone, width=15)
            pend_addtodone_btn.grid(row=3, column=0, padx=2, pady=5)

            backpend_btn = customtkinter.CTkButton(second_framePend, text="Back", fg_color="black",
                                                    hover_color="dark grey", border_width=2, corner_radius=6,
                                                    border_color="black", command=backpend)
            backpend_btn.grid(row=4, column=0, padx=5, pady=5)

            show_pend_lbl = Label(second_framePend, text=print_pend_rows_with_data, wraplength=1000000, justify="left",
                                   font=("Courier, 10"), bg="#292929", fg="silver")
            show_pend_lbl.grid(row=5, column=0, padx=5, pady=5)
#------------------------------------------------------------------------------------------------------------------------
        def plans_1():
            app2.withdraw()
            appPlans = customtkinter.CTkToplevel()
            appPlans.title("mummy's planner")
            appPlans.geometry("900x600")
            #appPlans.resizable(False, False)
            plans = sqlite3.connect("planning.db")
            recent_table = plans.cursor()
            show_plans = recent_table.execute("SELECT oid, plans FROM {} WHERE plans IS NOT NULL".format(input_username))
            shows_p = show_plans.fetchall()
            print_plans_rows_with_data = ""
            for record in shows_p:
                print_plans_rows_with_data += str(record[0]) + " " + str(record[1]) + " " + "\n"
            plans.commit()




            plans.commit()

#-------------------------------------------------------------------------------------------------------------------------
            def addtopending():
                info = plans_entry.get()
                try:
                    plans = sqlite3.connect("planning.db")
                    id = plans.cursor()
                    search = id.execute("SELECT plans FROM {} WHERE oid = {}".format(input_username, info))
                    inserter = search.fetchall()
                    inserting = ""
                    for insertValue in inserter:
                        inserting = str(insertValue[0])

                    insert_list = id.execute(
                        "UPDATE {} SET pending = :pend WHERE oid = {}".format(input_username, info),
                        {"pend": inserting,
                         })
                    result = []

                    # loop to add a new plan
                    for t in insert_list:
                        result.append(t)
                    plans.commit()
                    messagebox.showinfo("success", "The plan has been added to pending plans")

                except Exception as p:
                    messagebox.showerror("Oh no!", "The plan wasn't added, Try again")

#--------------------------------------------------------------------------------------------------------------------------------
            def backplans():
                appPlans.withdraw()
                app2.deiconify()
#------------------------------------------------------------------------------------------------------------------------------
            def updating():
                info = update_entry.get()
                plans = sqlite3.connect("planning.db")
                id = plans.cursor()
                search = id.execute("SELECT plans FROM {} WHERE oid = {}".format(input_username, info))
                inserter = search.fetchall()
                inserted = str(inserter[0])
                update_plan_frame = customtkinter.CTkFrame(second_framePlans, corner_radius=10)
                update_plan_frame.grid(row=7, column=0, padx=5, pady=5)

                update_plan_entry = Text(update_plan_frame, height=3, width=60, wrap=WORD, bd=1, bg="#292929",
                                         fg="silver", )
                update_plan_entry.pack(padx=10, pady=10)
                update_plan_entry.configure(insertbackground="white")
                update_plan_entry.insert(INSERT, inserted)
#------------------------------------------------------------------------------------------------------------------------------
                def updated():
                    info = update_entry.get()
                    try:
                        plans = sqlite3.connect("planning.db")
                        db = plans.cursor()


                        insert_list = db.execute("UPDATE {} SET plans = :plan WHERE oid = {}".format(input_username, info),
                                                 {"plan": update_plan_entry.get(1.0, "end-1c"),
                                                  })

                        result = []

                        # loop to add a new plan
                        for t in insert_list:
                            result.append(t[0])
                        plans.commit()
                        messagebox.showinfo("Success", "The Plan has been added and updated")
                    except Exception as u:
                        messagebox.showerror("Oh no!", "Failure in updating, try again")




                updating_btn = customtkinter.CTkButton(second_framePlans, text="Save", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                                 border_color="black", command=updated)
                updating_btn.grid(row=8, column=0, padx=5, pady=5)
#----------------------------------------------------------------------------------------------------------------------------


            #====================add scrollers=====================
            #create main frame
            main_frame = Frame(appPlans, bg="#292929")
            main_frame.pack(fill=BOTH, expand=1)

            #create a canvas
            my_canvas = Canvas(main_frame, bg="#292929")
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            #add scrollbar to the canvas
            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command= my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)


            #configure the canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

            #create another frame inside the canvas
            second_framePlans = Frame(my_canvas, bg="#292929")

            #add that new frame to a window in the canvas
            my_canvas.create_window((0,0), window=second_framePlans, anchor="nw")
#-------------------------------------------------------------------------------------------------------------------------
            #===============================create plans widget===============================
            plans_lbl = customtkinter.CTkLabel(second_framePlans, text="Plans", text_font=("Courier, 30"))
            plans_lbl.grid(row=0, column=0, pady=1, padx=1)

            user_id_plans_label = customtkinter.CTkLabel(second_framePlans, text="User: " + str(input_username), text_font=("Courier, 10"))
            user_id_plans_label.grid(row=1, column=0, padx=1, pady=1)

            plans_entry = customtkinter.CTkEntry(second_framePlans, border_width=2, placeholder_text="What number is the plan you want to add?",
                                                 corner_radius=6, width=300)
            plans_entry.grid(row=2, column=0, padx=5, pady=5)


            plans_addtoPending_btn = customtkinter.CTkButton(second_framePlans, text="Add to pending plans", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                               border_color="black", command=addtopending, width=15)
            plans_addtoPending_btn.grid(row=3, column=0, padx=2, pady=5)

            update_btn = customtkinter.CTkButton(second_framePlans, text="Edit", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                                 border_color="black", command=updating)
            update_btn.grid(row=5, column=0, padx=5, pady=5)

            update_entry = customtkinter.CTkEntry(second_framePlans, border_width=2,
                                                 placeholder_text="What number is the plan you want to edit?",
                                                 corner_radius=6, width=300)
            update_entry.grid(row=4, column=0, padx=5, pady=5)

            backplans_btn = customtkinter.CTkButton(second_framePlans, text="Back", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                               border_color="black", command=backplans)
            backplans_btn.grid(row=6, column=0, padx=5, pady=5)

            show_plans_lbl = Label(second_framePlans, text=print_plans_rows_with_data, wraplength=1000000, justify="left", font=("Courier, 10"), bg="#292929", fg="silver")
            show_plans_lbl.grid(row=9, column=0, padx=5, pady=5)

#------------------------------------------------------------------------------------------------------------------------------

        def doneapp():
            app2.withdraw()
            appdone = customtkinter.CTkToplevel()
            appdone.title("mummy's planner")
            appdone.geometry("900x600")
            # appPlans.resizable(False, False)
            plans = sqlite3.connect("planning.db")
            recent_table = plans.cursor()
            show_done = recent_table.execute("SELECT oid, done FROM {} WHERE done IS NOT NULL".format(input_username))
            shows_d = show_done.fetchall()
            print_done_rows_with_data = ""
            for record in shows_d:
                print_done_rows_with_data += str(record[0]) + " " + str(record[1]) + " " + "\n"
            plans.commit()

            plans.commit()

#-----------------------------------------------------------------------------------------------------------------------------


            def backdone():
                appdone.withdraw()
                app2.deiconify()
#-----------------------------------------------------------------------------------------------------------------------------
            # ====================add scrollers=====================
            # create main frame
            main_frame = Frame(appdone, bg="#292929")
            main_frame.pack(fill=BOTH, expand=1)

            # create a canvas
            my_canvas = Canvas(main_frame, bg="#292929")
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            # add scrollbar to the canvas
            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # configure the canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            # create another frame inside the canvas
            second_framedone = Frame(my_canvas, bg="#292929")

            # add that new frame to a window in the canvas
            my_canvas.create_window((0, 0), window=second_framedone, anchor="nw")
#-------------------------------------------------------------------------------------------------------------------------
            # ===============================create done widget===============================
            done_lbl = customtkinter.CTkLabel(second_framedone, text="Finished plans", text_font=("Courier, 30"))
            done_lbl.grid(row=0, column=0, pady=1, padx=1)

            user_id_done_label = customtkinter.CTkLabel(second_framedone, text="User: " + str(input_username),
                                                         text_font=("Courier, 10"))
            user_id_done_label.grid(row=1, column=0, padx=1, pady=1)





            backdone_btn = customtkinter.CTkButton(second_framedone, text="Back", fg_color="black",
                                                    hover_color="dark grey", border_width=2, corner_radius=6,
                                                    border_color="black", command=backdone)
            backdone_btn.grid(row=4, column=0, padx=5, pady=5)

            show_done_lbl = Label(second_framedone, text=print_done_rows_with_data, wraplength=1000000,
                                   justify="left", font=("Courier, 10"), bg="#292929", fg="silver")
            show_done_lbl.grid(row=5, column=0, padx=5, pady=5)



#-------------------------------------------------------------------------------------------------------------------------------





        #=======================================dashboard board widgets====================================================
        dashboard_label = customtkinter.CTkLabel(app2, text="DashBoard", text_font=("Courier, 30"))
        dashboard_label.place(x=5,anchor = NW)

        user_id_label = customtkinter.CTkLabel(app2, text="Current User :  " + str(input_username), text_font=("Courier, 10"))
        user_id_label.place(x=215, y=370)

        logout_btn = customtkinter.CTkButton(app2, text="Log out", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                               border_color="black", command=logout)
        logout_btn.place(x=5, y=370)

        planning_entry_label = customtkinter.CTkLabel(app2, text="What are your plans today?", text_font=("Courier, 10"))
        planning_entry_label.place( x=10, y=80)

        planning_entry_frame = customtkinter.CTkFrame(app2, corner_radius=10)
        planning_entry_frame.place(x=190, y=80)

        planning_entry = Text(planning_entry_frame, height=3, width=60, wrap=WORD, bd=0, bg="#292929", fg="silver", )
        planning_entry.pack(padx=10, pady=10)
        planning_entry.configure(insertbackground="white")

        add_entry_button =customtkinter.CTkButton(app2, text="Update", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                                  border_color="black", command=add, width=10)
        add_entry_button.place(x=695, y=80)

        reset_button = customtkinter.CTkButton(app2, text="Reset Database", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                               border_color="black", command=reset, width=15)
        reset_button.place(x=935, y=370)

        plans_btn = customtkinter.CTkButton(app2,text="Plans", fg_color="black", hover_color="dark grey", border_width=2, corner_radius=6,
                                               border_color="black", command=plans_1)
        plans_btn.place(x=150, y=200)

        pending_btn = customtkinter.CTkButton(app2, text="Pending plans", fg_color="black", hover_color="dark grey",
                                            border_width=2, corner_radius=6,
                                            border_color="black", command=pendingapp)
        pending_btn.place(x=350, y=200)

        done_btn = customtkinter.CTkButton(app2, text="Finished plans", fg_color="black", hover_color="dark grey",
                                              border_width=2, corner_radius=6,
                                              border_color="black", command=doneapp)
        done_btn.place(x=550, y=200)

#-------------------------------------------------------------------------------------------------------------------------------
        #CREATE CALENDER OPTION========================================================
        cal_lbl = customtkinter.CTkLabel(app2, text="Select the date of the plan", text_font=("Courier, 10"))
        cal_lbl.place(x=800, y=55)
        #today = the command to get the systems date
        today = date.today()
        dateOS = today.strftime("%d")
        convert_dateOS = int(dateOS)
        monthOS = today.strftime("%m")
        convert_monthOS = int(monthOS)
        yearOS = today.strftime("%Y")
        convert_yearOS = int(yearOS)
        #we display the calendar widget and set the automatic date to the system date
        cal = Calendar(app2, selectmode="day", year=convert_yearOS, month=convert_monthOS, day=convert_dateOS)
        cal.place(x=780, y=80)



"""/
=    /
 =    |   /
  =    |      /
   =    |         /
    =    |            /
     =    |               /
      =    |                  /
       =    |                     /
        =    |                        /
         =    |                           /
          =    |                              /
           =    |                                 /
            =    |                                    /
             =                                           /
              =                                              /
               =                                                 /
                =                                                    /
                 =                                                       /
                  =                                                          /
                   =                                                             /
                    =                                                                /
                     =                                                                   /
                      =                                                                      /
                       =                                                                         /
                        == ==================================================                                                                           /
=====================================================================================================
"""

# =======================login window============================
welcome_label = customtkinter.CTkLabel(app, text="Welcome to mummy's planner", text_font=("Courier, 15"))
welcome_label.place(relx=0.5, y =30, anchor=CENTER )

show_login_img_frame = customtkinter.CTkFrame(app, corner_radius=10, width=390, height=290)
show_login_img_frame.place(relx=0.5, y=200, anchor=CENTER)

login_img = PhotoImage(file = "C:/Users/admin/PycharmProjects/Mummy's planner project/plans_image/login_img2.png")
show_login_img = customtkinter.CTkLabel(show_login_img_frame, text="", image=login_img, bg_color="black", fg_color="black")
show_login_img.place(relx=0.5, y=140, anchor=CENTER)


login_entry = customtkinter.CTkEntry(app, border_width=2, placeholder_text="Enter your username", corner_radius=6, width=250)
login_entry.place(relx=0.5, y=400, anchor=CENTER)

login_btn = customtkinter.CTkButton(app, text="Login", corner_radius=6, border_width=2, border_color="black", fg_color="black", hover_color="dark grey",
                                    command=submit)
login_btn.place(relx=0.5, y=450, anchor=CENTER)
app.mainloop()