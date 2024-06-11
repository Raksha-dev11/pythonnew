#savefiles
'''from tkinter import *
from tkinter import filedialog

def saveFile():
    file=filedialog.asksaveasfile(
                                  defaultextension='.txt',
                                  filetypes=[
                                      ("Text file",".txt",
                                       "HTML file",".html",
                                       "All files",".*")
                                  ])
    filetext=str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window=Tk()
button = Button(text='save',command=saveFile)
button.pack()
text=Text(window)
text.pack()
window.mainloop()'''

#menubar
'''from tkinter import*

def openFile():
    print("File opened")
def saveFile():
    print("File saved")
def cutFile():
    print("You cut some text")
def copyFile():
    print("You copy some text")
def pasteFile():
    print("You paste some text")
window=Tk()

menubar=Menu(window)
window.config(menu=menubar)

fileMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cutFile)
editMenu.add_command(label="Copy",command=copyFile)
editMenu.add_command(label="Paste",command=pasteFile)

window.mainloop()'''

#frames
'''from tkinter import*
window=Tk()

frame=Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.pack()

Button(frame,text="W",font=("Consolas",20),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",20),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",20),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",20),width=3).pack(side=LEFT)


window.mainloop()
'''

#new windows
'''from tkinter import*

def create_window():
    new_window=Toplevel()

old_window=Tk()
Button(old_window,text="create new window",command=create_window).pack()
old_window.mainloop()'''

#windows tab
'''from tkinter import*
from tkinter import ttk
window=Tk()

notebook=ttk.Notebook(window)
tab1=Frame(notebook)
tab2=Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,ill="both")

Label(tab1,text="Hello,this is table1",width=50,height=25).pack()
Label(tab2,text="Goodbye,this is table2",width=50,height=25).pack()
window.mainloop()'''

#grid
'''from tkinter import *
window=Tk()

firstNameLabel=Label(window,text="First name: ",width=20,bg="red").grid(row=0,column=0)
firstNameEntry=Entry(window).grid(row=0,column=1)

lastNameLabel=Label(window,text="Last name: ",bg="green").grid(row=1,column=0)
lastNameEntry=Entry(window).grid(row=1,column=1)

emailLabel=Label(window,text="email: ",bg="blue").grid(row=2,column=0)
emailEntry=Entry(window).grid(row=2,column=1)

submitButton=Button(window,text="submit").grid(row=3,column=0,columnspan=2)
window.mainloop()'''

#progress bar
'''from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks=10
    x=0
    while(x<tasks):
      time.sleep(1)
      bar['value']+=10
      x+=1
      percent.set(str(int((x/tasks)*100))+"%")
      text.set(str(x)+"/"+str(tasks)+"tasks completed")
      window.update_idletasks()

window=Tk()

percent=StringVar()
text=StringVar()

bar= Progressbar(window,orient=HORIZONTAL,length=200)
bar.pack(pady=10)

percentLabel=Label(window,textvariable=percent).pack()
taskLabel=Label(window,textvariable=text).pack()
button = Button(window,text="download",command=start).pack()

window.mainloop()'''

#canvas
'''from tkinter import *
window=Tk()
canvas=Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="blue",width=5)
#canvas.create_line(0,500,500,0,fill="blue",width=5)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#points=[250,0,500,500,0,500]
#canvas.create_polygon(points,fill="yellow",outline="black",width=5)
#canvas.create_arc(0,0,500,500,fill="green",style=PIESLICE,start=270,width=5)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width="10")
canvas.pack()
window.mainloop()'''

#key events
'''from tkinter import*
def doSomething(event):
    #print("You pressed: ", event.keysym)
    label.config(text=event.keysym)

window=Tk()
window.bind("<Key>",doSomething)
label=Label(window,font=("Helvetica",100))
label.pack()
window.mainloop()'''

#mouse events
'''from tkinter import *

def doSomething(event):
    print("Mouse coordinates: ",event.x,",",event.y)

window=Tk()

window.bind("<Enter>",doSomething)
window.mainloop()'''

#drag&drop
'''from tkinter import*

def drag_start(event):
    label.startX=event.x
    label.startY=event.y
def drag_motion(event):
    x=label.winfo_x()-label.startX+event.x
    y=label.winfo_y()-label.startY+event.y
    label.place(x=x,y=y)

window=Tk()
label=Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)
window.mainloop()'''

#multiple animation
'''from tkinter import *
from balls import *
import time

window=Tk()

WIDTH=500
HEIGHT=500

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball= Ball(canvas,0,0,100,1,1,"white")
tennis_ball= Ball(canvas,0,0,50,4,3,"yellow")
basket_ball= Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()

    window.update()
    time.sleep(0.01)

window.mainloop()'''

#clock program
from tkinter import*
from time import *
def update():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%B %d,%Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window=Tk()

time_label=Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label=Label(window,font=("Ink Free",25))
day_label.pack()

date_label=Label(window,font=("Ink Free",30))
date_label.pack()


update()

window.mainloop()