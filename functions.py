print('--------------')
print('FUNCTIONS')
print('-------------')
# A function is a block of code which only runs when it is called.You can pass data, known as parameters, into a function.A function can return data as a result.
def first_function():
    print('Hello the first prime number is: ', 1 + 1)
first_function()
# Arguments
def info_func(f_name,l_name,age):
    print('My name is ' + f_name + " " + l_name +  ' and I am ' +  age + ' years old')
info_func("Hassan", "Bulega", "35")
# Arbitrary arguments , *args - This way the function will receive a tuple of arguments, and can access the items accordingly:
def siblings_func(*kids):
    print('His youngest sister are ', kids[2], kids[0])
siblings_func("Aisha","Asmaa","Aminah")
# Keyword Arguments(kwargs) => You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emy", child2 = "Tobias", child3 = "Linus")
# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes", alias = "TR")
# Default parameter
def my_function(country = "Uganda"):
  print("I am from " + country)

my_function("Sweden")
my_function()
# Passing a List as an Argument
def list_func(techStack):
   for x in techStack:
      print(x)
JS = ['mongodb','react','node','express']
list_func(JS)
# Return values
def return_func(x):
   return x ** 3
print(return_func(3),return_func(2))
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass
# Positional-Only Arguments - add , / after the arguments:
def my_function(x, /):
  print(x)

my_function(3) # my_function(x = 3) - throws an error
# Keyword-Only Arguments -  add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3) # my_function(3) - throws an error
print("-----------")
# RECURSION

# LAMBDA FUNCTIONS - A lambda function is a small anonymous function. It  can take any number of arguments, but can only have one expression.
x = lambda a : a + 11
print(x(10))
x = lambda a, b : a ** b
print(x(2,3))
# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))