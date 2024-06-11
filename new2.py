#modules
'''import messages 
messages.hello()
messages.bye()
#creating alias
import messages as msg
msg.hello()
msg.bye()
'''
'''
from messages import hello,bye
hello()
bye()'''


#help('modules')



#oop

'''class car:
    make=None
    model=None
    year=None
    color=None
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print("This car is driving")
    def stop(self):
        print ("this car is stopped")

obj=car()
'''


#inheritance
'''class Animal:
    alive=True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
rabbit=Rabbit()
fish=Fish()
hawk=Hawk()
print(rabbit.alive)
fish.eat()
rabbit.run()
fish.swim()
hawk.fly()
'''

#multi-level inheritance
'''class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog=Dog()
print(dog.alive)
dog.eat()
dog.bark()
'''




#multiple inheritance
'''class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")    

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator);
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
'''

#method overriding:
'''class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("THis rabbit is eating a carrot")
rabbit=Rabbit()
rabbit.eat()
'''



#method chaining
'''class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self

car=Car()
car.turn_on().drive().brake().turn_off()

'''

#super function

'''class Rectangle:
      def __init__ (self,length,width):
        self.length=length
        self.width=width
class Square(Rectangle):
    def __init__ (self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__ (self,length,width,height):
        super().__init__(length,width)
        self.height=height
    def volume(self):
        return self.length*self.width*self.height
    


square=Square(3,3)
cube=Cube(3,3,3)   
print(square.area())
print(cube.volume())
'''


#object as arguments
'''class Car:
    color=None
class Motorcycle:
    color=None
def change_color(vehicle,color):
    vehicle.color=color
car1=Car()
car2=Car()
car3=Car()

bike1=Motorcycle()

change_color=(car1,"red")
change_color=(car2,"white")
change_color=(car3,"blue")
change_color=(bike1,"black")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)

'''

#duck typing
'''class Duck:
    def walk(self):
        print("This duckk is walking")
    def talk(self):
        print("This duck is qwacking")
class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")
class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")
duck=Duck()
chicken=Chicken()
person=Person()
person.catch(chicken)
'''
#walrus operator
'''print(happy:=True)

foods=list()
while food := input("what food do you like?: ") !="quit":
    foods.append(food)
'''

#function to a variable
'''def hello():
    print("Hello")
print(hello)


say=print
say("it works")

'''



#lambda function

#def double(x):
#   return x*2
#print(double(5))
#this can be written as
'''double = lambda x:x*2
multiply=lambda x,y,z:x*y*z
print (multiply(5,6,7))

'''

#sort method
'''students = ("Ram","Varun","Rohan")
#students.sort()#only can be used for lists
sorted_students=sorted(students)
for i in students:
    print(i)

students=[("Ram","F",60),
          ("Varun","A",33),
          ("Rohan","D",36)]
grade=lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print (i)
'''

#map() function
'''store=[("shirt",20.00),
       ("pants",25.00),
       ("jacket",50.00),
       ("socks",10.00)]
to_euros=lambda data:(data[0],data[1]*0.82)
store_euros=list(map(to_euros,store))
for i in store_euros:
    print(i)
'''

#filter function
'''friends=[("Rachel",19),
         ("Monica",18),
         ("joey",16),
         ("Ross",20)]
age=lambda data:data[1]>=18
vote=list(filter (age,friends))
for i in vote:
    print(i)
'''




#reduce function
'''import functools
letters=["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letters)
print (word)
'''




























