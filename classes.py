print('--------------')
print('CLASSES')
print('-------------')
# A Class is like an object constructor, or a "blueprint" for creating objects.
class Car:
    name = "vehicle"
    sitting_capacity = 7
wish = Car()
print(wish.sitting_capacity)
# The __init__() Function - All classes have a function called __init__(), which is always executed when the class is being initiated.Use the __init__() function to assign values to object properties.

class Beautiful:
    def __init__(self,name,age,color): # use the __init__() function to assign values for name and age:
        self.name = name
        self.age = age
        self.color = color
    def descrip(self): # object method
        print("Hello my name is Queen " + self.name )

b1 = Beautiful('Mulungi',21,"brown")
print('She is ' + b1.color + " " +  b1.name + " at ", b1.age)
b1.descrip()
# The __init__() function is called automatically every time the class is being used to create a new object.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# change properties
b1.age = 19
print('She is ' + b1.color + " " +  b1.name + " at ", b1.age)

del b1.color # delete property or del b1 - which deletes the object

# Python Inheritance
print('Inheritance\n -------------')
class Person: # Parent class created like any other class
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

p2 = Person('Wamala','Abubakar')
p2.printname()
class Student(Person): # child class created by passing parent as a parameter
    pass
s1 = Student('Muhsin','Muusaa')
s1.printname()

class Student(Person):
  def __init__(self, fname, lname): # When you add the __init__() func, the child class will nolonger inherit the parent's __init__() function.
      print('child nolonger inherits from parent')

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# Add properties and methods to the child class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s3 = Student('Kayemba','Rayan',2031)
s3.welcome()
print('Polymorphism\n -------------')
# Polymorphism - refers to methods/functions with the same name that can be executed on many objects or classes.
#  Function polymorphism e.g the len() function which can be used to find length of a list,string,tuple and dictionary

# Class polymorphism - example, three classes Car,Plane,Boat can have a method move()
class Car:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model

   def move(self):
      print('Drive')
      
class Boat:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model

   def move(self):
      print('Sail')

class Plane:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model

   def move(self):
      print('Fly')

car1 = Car('Ford','Mustang')
boat1 = Boat('Lyato','Pya')
plane1 = Plane('Endeege','Kapyaata')

for x in (car1,boat1,plane1):
   x.move()
# Inheritance class plymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle): # inherits vehicle class properties and method
  pass
# Boat and plane inherit brand,model and move() from vehicle but override the move()
class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1,boat1,plane1):
   print(x.brand)
   print(x.model)
   x.move()
   