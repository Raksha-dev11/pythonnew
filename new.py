'''food=["pizza","burger","noodles"]
food[0]="sushi"
print(food[0])



#functions in list
food.append("ice cream")
food.remove("noodles")
food.pop()
food.sort()
food.insert(0,"cake") 
food.clear()

for x in food:
    print(x)
'''

'''drinks=["coffee","soda","tea"]
dinner=["pizza","hamburger","hotdog"]
dessert=["cake","ice cream"]

food = [drinks,dessert,dinner]
print(food[0][0])
print(food[1][1])
print(food[2][1])'''


#tuples
'''student=("dia",21,"female")
print(student.count("dia"))
print(student.index[0])

for x in student:
    print(x)
if "dia" in student:
    print("dia is here")   '''


#set
'''utensils={"fork","spoon","knife"}
dishes={"bowl","plate","cup","knife"}
utensils.add("napkin")
utensils.remove("fork")
utensils.clear()

dishes.update(utensils)
dinner_table=utensils.union()

 
print(utensils.difference(utensils))
print(utensils.intersection(dishes))
for x in utensils:
    print(x)'''




#dictionary
'''capitals={'USA':'Washington DC',
          'India':'New Delhi',
          'China':'Beijing',
          'Russia':'Moscow'
          }

capitals.upadte({'Germany':'Berlin'})
capitals.upadte({'USA':'Las Vegas'})
print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,values in capitals.items():
    print(key,values)'''




'''name="bro Code"
if(name[0].islower()):
    name=name.capitalize()
print(name)    

first_name=name[0:3].upper()
print(first_name)
last_name=name[4:].lower()
print(last_name)
last_character=name[-1]
print(last_character)'''


#functions
'''def hello(name):
      print("hello!"+name)
hello("hey")      
hello("Dude")


def hello(first_name,last_name,age):
      print("hello "+first_name+" "+last_name)
      print("You are "+str(age)+" years old")
      print("Have a nice day!")
hello("Bro","Code",21)      
'''


#return statement
'''def multilply(num1,num2):
    result=num1+num2
    return result
print(multilply(6,8))'''

#keyword arguments
'''def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)

hello(last="Code",middle="Dude",first="bro")'''


#nested function calls
#print(round(abs(float(input("Enter a whole positive num: ")))))


#scope
'''name="bro" #global scope(available inside and outside functions)
def display_name():
    name="code"  #local scope(available only inside this function)
    print(name)
display_name()
print(name)
'''

#*args

'''def add(*stuff):
    sum=0
    stuff=list(stuff)
    stuff[0]=0
    for i in stuff:
        sum+=i
    return sum
print(add(1,2,3,4,5,6))
'''


#**kwargs:
'''def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(first="Bro",middle="Dude",last="Code")        
'''


#format method
'''animal="cow"
item="moon"
print("the {} jumnped over the {}".format(animal,item))
'''


'''import random

mylist=['rock','scissor','paper']
z=random.choice(mylist)
cards=[1,2,3,4,5,6,7,8,9,'j','q','k','a']
random.shuffle(cards)
print(cards)
'''

#exception
'''try:
    num=int(input("enter a num to divide: "))
    den=int(input("enter a num to divide by: "))
    result=num/den
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero")
except ValueError as e:
    print(e)
    print("enter only num")
except Exception as e:
    print(e)
    print("something went wrong")
'''



'''import os
path="C:\\Users\\raksh\\OneDrive\\Desktop\\text.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
else:
    print("That location doesnt exist!")
'''


'''with open('text.txt') as file:
    print(file.read())

'''

#to write new text
'''text="This is some text"
with open('text.txt','w') as file:
    file.write(text)
'''

#to append
'''text ="have a nice day!"
with open('text.txt','a')as file:
    file.write(text)

'''

#copying files
'''import shutil
shutil.copyfile('text.txt','copy.txt') '''

#move files
'''import os
source="text.txt "
destination="C:\\Users\\raksh\\OneDrive\\Desktop\\text.txt"
if os.path.exists(destination):
    print("There is already a file there")
else:
    os.replace(source,destination)
    print(source+" was moved")
'''

#delete files
'''import os
os.remove("C:\\Users\\raksh\\OneDrive\\Desktop\\text.txt")
'''


















