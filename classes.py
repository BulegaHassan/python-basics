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
