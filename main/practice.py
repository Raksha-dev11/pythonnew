'''name="Bro finds"
print(len(name))
print(name.find("B"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","i"))
print(name*6) 
'''



'''#type casting
x =1 #int
y =2.0 #float
z ="3" #string
z=int(z) #changes its data type permanently
print(int(y)) #change its data type for once
print(z*3)
print(float(x))'''


'''#allow user to input values
name = input("What is your name? ")
age = int(input ("How old are you? "))
height=float(input("How tall are you? "))
age=age+1
print("Hello "+name )

print("You are ",(age)," years old")
print ("You are ",height," cm tall")'''



'''#math functions
import math
pi=-3.14
x=1
y=2
z=3
print( round(pi))
print(math.ceil(pi))
print(math.abs(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))
print(min(x,y,z))'''



'''#string slicing
name= "Raksha Thakur"
first_name = name[0:6]
print(first_name)
last_name=name[7:12]
print(last_name)

funky_name=name[0:12:2]
print(funky_name)
reversed_name=name[::-1]
print(reversed_name) '''

website="http://google.com"
slice=slice(7,-4)
print(website[slice])

