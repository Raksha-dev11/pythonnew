#list comprehension
'''square=[i*i for i in range(1,11)]
print(square)

students=[100,90,80,70,60,50,40,30,20,10]
passed__students=[i for i in students if i>=60]
print(passed__students)'''

#dictinary comprehension
'''tempF = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
tempC={key:round((value-32)*(5/9)) for (key,value) in tempF.items()}
print(tempC)

weather={'New York':"snowing",'Boston':"sunny",'Los Angeles':"sunny",'Chicago':"cloudy"}
sunny_weather={key:value for (key,value) in weather.items() if value=="sunny"}
print(sunny_weather)'''

#zip() function
'''usernames=["Dude","Bro","Mister"]
passwords=("password","abc123","guest")
users=zip(usernames,passwords)
print(type(users))
for i in users:
    print (i)'''

#if __name__ == '__main__'
'''if __name__ == '__main__':
    print("running this module directly")
else:
    print("running this module indirectly")'''

#time 
#import time
'''print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))
time_obj=time.localtime()#local time
time_obj=time.gmtime()#UTC time
print(time_obj)
local_time=time.strftime("%B %d %Y %H:%M:%S ",time_obj)
print(local_time)'''

'''time_string="20 April,2020"
time_obj = time.strptime(time_string,"%d %B,%Y")
print(time_obj)'''

#threading
'''import threading
import time

def eat():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x=threading.Thread(target=eat,args=())
x.start()
y=threading.Thread(target=drink_coffee,args=())
y.start()
z=threading.Thread(target=study,args=())
z.start()
#eat()
#drink_coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())'''

#daemon thread
'''import threading
import time
def timer():
    print()
    time.sleep(1)
    count=0
    while True:
        time.sleep(1)
        count+=1
        print("logged in for:" ,count, "seconds")
x = threading.Thread(target=timer,daemon=True)
x.start()
answer=input("Do you wish to exit? ")
'''

#multiprocessing
'''from multiprocessing import Process,cpu_count
import time
def counter(num):
    count=0
    while(count<num):
        count+=1
def main():
    print(cpu_count())
    a=Process(target=counter,args=(10000000000,))
    a.start()
    a.join()
    print("finished in:", time.perf_counter(),"seconds")

if __name__=='__main__':
    main()
'''

#GUI
'''from tkinter import*

window= Tk() #instantiate an instance of  window
window.title("Raksha first Gui program")
window.config(background="black")
window.mainloop() #place window on computer screen
'''
'''from tkinter import *
window = Tk()

label = Label(window,text="Hello World",
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,)
#label.place(x=0, y=0)
label.pack()

window.mainloop()
'''
#button
'''from tkinter import *
def click():
    print("You clicked the button!")

window = Tk()
photo= PhotoImage(file='C:\\Users\\raksh\\Downloads\\thumbs up.jpg')
button=Button(window,
              text="click me!",
              command=click,
              font=("Comic Sans",30),
              fg="green",
              bg="black",
              activeforeground="green",
              activebackground="black",
              image=photo)
button.pack()
window.mainloop()
'''

#entrybox
'''from tkinter import*
def submit():
    username=entry.get()
    print("Hello",username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
                

window= Tk()
entry = Entry(window,
              font=("Arial",50),
              fg="green",
              bg="black",
              show="*")
#entry.insert(0,'hello')
entry.pack(side=LEFT)
submit_button=Button(window,
                     text="submit",
                     command=submit)
submit_button.pack(side=RIGHT)
del_button=Button(window,
                     text="delete",
                     command=delete)
del_button.pack(side=RIGHT)
backspace_button=Button(window,
                     text="backspace",
                     command=backspace)
backspace_button.pack(side=RIGHT)
window.mainloop()'''

#check buttons
'''from tkinter import*

def display():
    if (x.get()==1): 
        print("You agree!")
    else:
        print("You don't agree!")
window= Tk()

x= IntVar()
check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg="green",
                           bg="black",
                           activeforeground="green",
                           activebackground="black",
                           padx=25,
                           pady=25)
check_button.pack()
window.mainloop()'''

#radiobuttons
'''from tkinter import*
food=["pizza","hamburger","hotdog"]
def order():
    if(x.get()==0):
        print("You ordered pizza:")
    elif(x.get()==1):
        print("You ordered a hamburger")
    elif(x.get()==2):
        print("You ordered a hotdog:")
    else:
        print("huh?")
window= Tk()
x=IntVar()
for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index],
                            variable=x,
                            value=index,
                            padx=25,
                            font=('Impact',50),
                            indicatoron=0,
                            width=175,
                            command=order)
    radiobutton.pack(anchor=W)
window.mainloop()
'''
#sliding scale
'''from tkinter import *
def submit():
    print("The temperature is: ",scale.get(), "degrees C")

window=Tk()
scale= Scale(window,
             from_=100,
             to=0,
             length=400,
             orient=VERTICAL,
             font=('Consolas',20),
             tickinterval=10,
             resolution=5,
             troughcolor="blue",
             fg="red",
             bg="black"
             )
scale.pack()
button=Button(window,
              text='submit',
              command=submit)
window.mainloop()'''


#listbox
'''def submit():
   food=[]
   for index in listbox.curselection():
      food.insert(index,listbox.get(IndexError))
   print("You have ordered: ")
   for index in food:
      print(index)
   #print(listbox.get(listbox.curselection()))

def add():
   listbox.insert(listbox.size(),entryBox.get())
   listbox.config(height=listbox.size())   

def delete():
   for index in reversed(listbox.curselection()):
      listbox.delete(index)
   #listbox.delete(listbox.curselection())
   listbox.config(height=listbox.size())

from tkinter import *

window=Tk()

listbox=Listbox(window,
                bg="#EFC3D2",
                font=("Constantia",25),
                width=10,
                selectmode="multiple")
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"soup")
listbox.insert(4,"salad")
listbox.insert(5,"tacos")

listbox.config(height=listbox.size())

entryBox=Entry(window)
entryBox.pack()

submitButton=Button(window,text="submit",command=submit)
submitButton.pack()

addButton=Button(window,text="add",command=add)
addButton.pack()

deleteButton=Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop()'''

#messagebox
'''from tkinter import*
from tkinter import messagebox

def click():
  # if messagebox.askyesno(title='ask yes or no',message='Do you like cake'):
   #   print('I like cake too: ')
   #else:
    #print('Why do you not like cake? ')
    answer=messagebox.askyesnocancel(title='Yes no cancel',message='Do you like to code?')
    if(answer==True):
        print("You like to code")
    elif(answer==False):
        print("You dont like to code")
    else:
        print("You have dodged the question")
    #print( messagebox.askquestion(title='ask question',message='Do you like pie?'))
    #messagebox.showinfo(title='This is an info message box',message='you are a person')
window=Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()'''

#colorimport module
'''from tkinter import *
from tkinter import colorchooser

def click():
    
    window.config(bg=colorchooser.askcolor()[1])

window=Tk()
window.geometry("420x420")
button=Button(text='click me',command=click)
button.pack()
window.mainloop()
'''

#textwidget
'''from tkinter import*

def submit():
    input=text.get("1.0",END)
    print(input)
  
window=Tk()
text=Text(window,
          bg='light yellow',
          font=('Ink Free',20),
          height=8,
          width=20,
          padx=20,
          pady=20,
          fg="purple")
text.pack()
button=Button(window,text="submit",command=submit)
button.pack()
window.mainloop()'''

#File dialog
'''from tkinter import*
from tkinter import filedialog

def openFile():
    filepath=filedialog.askopenfilename()
    file = open(filepath,'r')
    print(file.read())
    file.close
window=Tk()
button = Button(text="open",command=openFile)
button.pack()
window.mainloop()
'''