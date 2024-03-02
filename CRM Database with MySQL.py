from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import messagebox
from tkinter import ttk


app = Tk()
app.title("CRM database")
app.geometry("400x400")

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "Ugochukwuak12%",
    database ="codemy"
)

#print(mydb)---------#checked to see if the connection was succesfull

#Create a cursor and initialize
my_cursor = mydb.cursor()

#create database...====================================
my_cursor.execute("CREATE DATABASE IF NOT EXISTS codemy")
#----------------------------------------------------------------------------------

#test if the database created was successfull=============================================
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
 #   print(db)
#-----------------------------------------------------------------------------------------


#create a table...=============================================
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255), last_name VARCHAR(255), zipcode INT(10), price_paid DECIMAL(10, 2), user_id INT AUTO_INCREMENT PRIMARY KEY)")
#------------------------------------------------------------------------------------------


#test to see if the table was created======================================
#my_cursor.execute("SELECT * FROM customers")
#for thing in my_cursor.description:
   # print(thing)
#--------------------------------------------------------------------------


#Clear text fields
def clear_fields():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    zipcode_name_entry.delete(0, END)
    price_paid_entry.delete(0, END)

#-------------------------------------------------------------------------------------------------------------------------
#submite to database
def add_customer():
    #command to add stuff to the database created (%s) is an instance just an assumption of the data
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid)  VALUES (%s, %s, %s, %s)"
    values = (first_name_entry.get(),
              last_name_entry.get(),
              zipcode_name_entry.get(),
              price_paid_entry.get())
    my_cursor.execute(sql_command, values)


    #commit changes to database
    mydb.commit()
    clear_fields()
#----------------------------------------------------------------------------------------------------------------------------

#write to csv(excel) function
def write_to_csv(result):
    with open("customers.csv", "a") as f:
        w = csv.writer(f, dialect="excel")
        w.writerow(result)
#----------------------------------------------------------------------------------------------------------------------------

#show what is in the database
def show_database():
    app.withdraw()
    app2 = Tk()
    app2.title("Show Database")
    app2.geometry("400x600")

    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    #a loop to list all in the database and number them
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_lbl = Label(app2, text=y)
            lookup_lbl.grid(row=index, column=num)
            num += 1
            print(x)
    csv_button = Button(app2, text="Save to Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0) #ignore the highlighted index

#------------------------------------------------------------------------------------------------------------------------

#search customers
def search_customers():
    app.withdraw()
    app3 = Tk()
    app3.title("Search customers")
    app3.geometry("550x400")

    def save_edit():
        pass

    def edit_now(id_ref, index):
        sql2 = "SELECT * FROM customers"
        searched = search_entry.get()
        name = (searched,)

        # create labels
        index +=1
        first_name_lbl = Label(app3, text="First Name").grid(row=index+3, column=0, sticky=W, padx=10, pady=10)
        last_name_lbl = Label(app3, text="Last Name").grid(row=index+4, column=0, sticky=W, padx=10)
        zipcode_lbl = Label(app3, text="Zipcode").grid(row=index+5, column=0, sticky=W, padx=10)
        price_paid_lbl = Label(app3, text="Price paid").grid(row=index+6, column=0, sticky=W, padx=10)

        # create entry boxes
        global first_name_entry
        first_name_entry2 = Entry(app3)
        first_name_entry2.grid(row=index+3, column=1, pady=5)
        global last_name_entry
        last_name_entry2 = Entry(app3)
        last_name_entry2.grid(row=index+4, column=1, pady=5)
        global zipcode_name_entry
        zipcode_name_entry2 = Entry(app3)
        zipcode_name_entry2.grid(row=index+5, column=1, pady=5)
        global price_paid_entry
        price_paid_entry2 = Entry(app3)
        price_paid_entry2.grid(row=index+6, column=1, pady=5)

        save_edit_btn = Button(app3, text="Save edit", command=save_edit)
        save_edit_btn.grid(row=index+7, column=0,  pady=5)


    def search_now():
        selected = drop.get()
        if selected == "Search by...":
            messagebox.showerror("Error", "Forgot to pick a thing!")

        if selected ==  "First Name":
            sql = "SELECT * FROM customers WHERE first_name = %s"
            searched = search_entry.get()
            name = (searched,)
            result = my_cursor.execute(sql, name)
            result = my_cursor.fetchall()
            #loop to list the result in a neat looking way
            for index, x in enumerate(result):
                num = 0
                #to show the number of the list
                id_ref = str(x[4])
                for y in x:

                    lookup_lbl = Label(app3, text=y)
                    lookup_lbl.grid(row=index + 2, column=num+1, pady=10)
                    edit_btn = Button(app3, text="Edit",command=lambda:edit_now(id_ref, index)) #the lambda is to pass the id_ref in and make sure it edits the
                    #right data
                    edit_btn.grid(row=index+2, column=0, pady=10)
                    num += 1

            if not result:
                messagebox.showerror("Oh No!", "Record not found....")

        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
            searched = search_entry.get()
            name = (searched,)
            result = my_cursor.execute(sql, name)
            result = my_cursor.fetchall()
            # loop to list the result in a neat looking way
            for index, x in enumerate(result):
                num = 0
                for y in x:
                    lookup_lbl = Label(app3, text=y)
                    lookup_lbl.grid(row=index + 2, column=num)
                    edit_btn = Button(app3, text="Edit", command=lambda: edit_now(id_ref,
                                                                                  index))  # the lambda is to pass the id_ref in and make sure it edits the
                    # right data
                    edit_btn.grid(row=index + 2, column=0, pady=10)
                    num += 1
            if not result:
                messagebox.showerror("Oh No!", "Record not found....")

    



    #search entry box
    search_entry = Entry(app3)
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    search_entry_lbl = Label(app3, text="Search")
    search_entry_lbl.grid(row=0, column=0, padx=10, pady=10)

    search_entry_btn = Button(app3, text="Search Customers", command=search_now)
    search_entry_btn.grid(row=1, column=0, padx=10)

    #search drop down box
    drop = ttk.Combobox(app3, value=["Search by...", "First Name", "Last Name"])
    drop.current(0)
    drop.grid(row=0, column=2 )


#-----------------------------------------------------------------------------------------------------------------------------

#create labels
title_lbl = Label(app, text="Codemy Customer Database", font=("Helvetica, 16"))
title_lbl.grid(row=0, column=0, columnspan=2, pady=10)

first_name_lbl = Label(app, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_lbl = Label(app, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
zipcode_lbl = Label(app, text="Zipcode").grid(row=3, column=0, sticky=W, padx=10)
price_paid_lbl = Label(app, text="Price paid").grid(row=4, column=0, sticky=W, padx=10)

#create entry boxes
first_name_entry = Entry(app)
first_name_entry.grid(row=1, column=1, pady=5)

last_name_entry = Entry(app)
last_name_entry.grid(row=2, column=1, pady=5)

zipcode_name_entry = Entry(app)
zipcode_name_entry.grid(row=3, column=1, pady=5)

price_paid_entry = Entry(app)
price_paid_entry.grid(row=4, column=1, pady=5)

#create buttons
add_customer_btn = Button(app, text="Add customer to database", command=add_customer)
add_customer_btn.grid(row=5, column=0, padx=10, pady=10)

clear_fields_btn = Button(app, text="Clear fields", command=clear_fields)
clear_fields_btn.grid(row=5, column=1, padx=10, pady=10)

show_btn = Button(app, text="Show databse", command=show_database)
show_btn.grid(row=6, column=0, sticky=W, padx=10, pady=10)

search_btn = Button(app, text="Search/Edit Customers", command=search_customers)
search_btn.grid(row=6, column=1, sticky=W, padx=10)




app.mainloop()