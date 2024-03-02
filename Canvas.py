from tkinter import *

app =Tk()
app.title("Canvases")
app.geometry("600x600")

W= 600
H = 400
x = W/2
y= H/2

my_canvas = Canvas(app, width=W, height=H, bg="white")
my_canvas.pack(pady=20)


#creat line------------------------------------------
#my_canvas.create_line(x1, y1, x2, y2, <- this are the coordinates .....fill="color"
#using a graph to show you:
"""
  Y
  |300
  |
  |
  |200
  |
  |
  |100
  |
  |                           
  0---------------------------->X
       100     200      300
"""
'''my_canvas.create_line(0, 100, 300, 100, fill="white")
my_canvas.create_line(150, 0, 150, 200, fill="white")'''

#Rectangle---------------------------------------------------------
#my_canvas.create_rectangle(x1, y1, x2, y2, fill="color")
#Rectangle-x1, y1: Top Left
#Rectangle-x2, y2: Bottom Right
#using a graph to show you:
"""
  Y
  |300
  |
  |
  |200
  |
  |
  |100
  |
  |                           
  0---------------------------->X
       100     200      300
"""
"""my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")"""

#create elipse(oval)----------------------------------------------------
#Oval-x1, y1: Top Left
#Oval-x2, y2: Bottom Right
#basically we are creating a rectangle and fitting an oval into it
"""my_canvas.create_oval(50, 150, 250, 50, fill="cyan")"""

#MOVE OBJECTS/CANVAS AROUND THE SCREEN WITH THE ARROW KEYS===============================================
"""
my_circle = my_canvas.create_oval(x, y, x+10, y+10, fill="cyan")
def left(event):
    #command to move canvases setting the distance of x and y and assigning them
    x= -10
    y = 0
    my_canvas.move(my_circle, x, y)
def right(event):
    #command to move canvases setting the distance of x and y and assigning them
    x= 10
    y = 0
    my_canvas.move(my_circle, x, y)
def up(event):
    #command to move canvases setting the distance of x and y and assigning them
    x=  0
    y = -10
    my_canvas.move(my_circle, x, y)
def down(event):
    #command to move canvases setting the distance of x and y and assigning them
    x=  0
    y = 10
    my_canvas.move(my_circle, x, y)
app.bind("<Left>", left)
app.bind("<Right>", right)
app.bind("<Up>", up)
app.bind("<Down>", down)
"""

#ADDING IMAGES TO OUR CANVAS WITH KEYS=============================================
"""img = PhotoImage(file="C:/Users/admin/PycharmProjects/How to code with Tkinter/images/ptp.png")
my_image = my_canvas.create_image(0,0, anchor=NW, image=img)"""

#MOVING OBJECTS ON YOUR CANVAS WITH YOUR MOUSE========================================
img = PhotoImage(file="C:/Users/admin/PycharmProjects/How to code with Tkinter/images/ptp.png")
my_image = my_canvas.create_image(0,0, anchor=NW, image=img)

def move(event):
    #event.x
    #event.y this are the event variables we passed and the x, y shows the x and y positions of the mouse when each event is passed
    global img
    img = PhotoImage(file="C:/Users/admin/PycharmProjects/How to code with Tkinter/images/ptp.png")
    my_image = my_canvas.create_image(event.x, event.y, image=img)
    mouse_lbl.config(text="Coordinates: x:" + str(event.x) + "  y:" + str(event.y))




my_canvas.bind("<B1-Motion>", move)
mouse_lbl = Label(app, text="")
mouse_lbl.pack(pady=20)


app.mainloop()