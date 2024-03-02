from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

app = Tk()
app.title("Using Databases")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")
app.geometry("400x600")

#create a database or connect to one
#to connect one:
#com = sqlite3.connect("address_book.db")
#create a cursor:
#c = com.cursor()


#create table
#c.execute("CREATE TABLE addresses(first_name text, "
          #"last_name text, "
          #"address text, "
          #"city text, "
          #"state text, "
          #"zipcode integer)")

#commit changes:
#com.commit()
#close connection
#com.close()

def update():
    com = sqlite3.connect("address_book.db")
    c = com.cursor()


    #to update your table
    record_id = delete_box.get()
    c.execute("UPDATE addresses SET "
              "first_name = :first, "
              "last_name = :last, "
              "address = :address, "
              "city = :city, "
              "state = :state, "
              "zipcode = :zipcode "
              
              "WHERE oid = :oid",

              {"first" : f_name_edit.get(),
               "last" : l_name_edit.get(),
               "address" : address_edit.get(),
               "city" : city_edit.get(),
               "state" : state_edit.get(),
               "zipcode" : zipcode_edit.get(),
               "oid" : record_id

              })



    com.commit()
    com.close()
    msgbox = messagebox.showinfo(" ", "Record has been updated")
    editor.destroy()

#create function to edit
def edit():
    global editor
    editor = Tk()
    editor.title("Edit data")
    editor.iconbitmap("C:/Users/admin/Pictures/company.ico")
    editor.geometry("400x300")

    com = sqlite3.connect("address_book.db")
    c = com.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    #create global variables for textbox names
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit


    # create textboxes
    f_name_edit = Entry(editor, width=30)
    f_name_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_edit = Entry(editor, width=30)
    l_name_edit.grid(row=1, column=1)

    address_edit = Entry(editor, width=30)
    address_edit.grid(row=2, column=1)

    city_edit = Entry(editor, width=30)
    city_edit.grid(row=3, column=1)

    state_edit = Entry(editor, width=30)
    state_edit.grid(row=4, column=1)

    zipcode_edit = Entry(editor, width=30)
    zipcode_edit.grid(row=5, column=1)

    #loop to insert the info into entry boxes
    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        zipcode_edit.insert(0, record[5])

    # create textbox labels
    f_namelbl = Label(editor, text="Firstname")
    f_namelbl.grid(row=0, column=0, pady=(10, 0))

    l_namelbl = Label(editor, text="Lastname")
    l_namelbl.grid(row=1, column=0)

    addresslbl = Label(editor, text="Address")
    addresslbl.grid(row=2, column=0)

    citylbl = Label(editor, text="City")
    citylbl.grid(row=3, column=0)

    statelbl = Label(editor, text="State")
    statelbl.grid(row=4, column=0)

    zipcodelbl = Label(editor, text="Zipcode")
    zipcodelbl.grid(row=5, column=0)

    #create a save button for edit
    save_btn = Button(editor, text="Save Record", command=update,)
    save_btn.grid(row=6,column=0, pady=10, padx=10)


#create function to delete a record
def delete():
    com = sqlite3.connect("address_book.db")
    c = com.cursor()
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    com.commit()
    com.close()


def submit():
    # add sqlite3 function
    com = sqlite3.connect("address_book.db")
    c = com.cursor()
    # insert into our table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {"f_name": f_name.get(),
               "l_name": l_name.get(),
               "address": address.get(),
               "city": city.get(),
               "state": state.get(),
               "zipcode": zipcode.get()})

    com.commit()
    com.close()
    #clear textbox after submittion
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)









#create query function
def query():
    com = sqlite3.connect("address_book.db")
    c = com.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    #loop thru results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +  str(record[6]) + "\n"
        print(print_records)

    query_label = Label(app, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    com.commit()
    com.close()




#create textboxes
f_name = Entry(app, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(app, width=30)
l_name.grid(row=1, column=1)

address = Entry(app, width=30)
address.grid(row=2, column=1)

city = Entry(app, width=30)
city.grid(row=3, column=1)

state = Entry(app, width=30)
state.grid(row=4, column=1)

zipcode = Entry(app, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(app, width=30)
delete_box.grid(row=9, column=1)


#create textbox labels
f_namelbl = Label(app, text="Firstname")
f_namelbl.grid(row=0, column=0, pady=(10,0))

l_namelbl = Label(app, text="Lastname")
l_namelbl.grid(row=1, column=0)

addresslbl = Label(app, text="Address")
addresslbl.grid(row=2, column=0)

citylbl = Label(app, text="City")
citylbl.grid(row=3, column=0)

statelbl = Label(app, text="State")
statelbl.grid(row=4, column=0)

zipcodelbl = Label(app, text="Zipcode")
zipcodelbl.grid(row=5, column=0)

delete_boxlbl = Label(app, text="Select ID")
delete_boxlbl.grid(row=9, column=0)

#create submit button
submit_btn = Button(app, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create a querry button to show records
query_btn = Button(app, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10,padx=10, ipadx=137)

#create delete button
delete_btn = Button(app, text="Delete a record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

#create an update button
edit_btn = Button(app, text="Edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=50, )



app.mainloop()