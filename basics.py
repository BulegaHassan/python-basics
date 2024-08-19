# order of execution
print('line1')
print('line2')
print('line3') 

# # pythogaros theorem
# adjacent = int(input('Please enter a value: '))
# opposite = int(input('Please enter a value: '))
# hypotenuse = (pow(adjacent,2) + pow(opposite,2)) ** (1/2)
# print('The hypotenuse is: ', hypotenuse)


# Python indentation 
if 5 > 2:
    print('Five is greater than 2')

# Single line comment
'''
This is a 
multline comment
but single line comments preceded it
'''
# assign variables 
x = 'apple'
y = 31
z = 49
a,b,c = 'apple', ' is not ', 'cherry' # multiple values in one line
d=e=f= 'fruit' # one value to multiple variables in a single line
print(x,y,a,b,c,d,e,f)

# output variables
print(a,b,c)
print(a+b+c)
print(y + z)

# Data types
s = "I am a Muslim" # str
i = 31 # int
f = 30.2 #float
c = 2j # complex
myList = ['apple','banana','cherry'] # list
myTuple = ('apple','banana','cherry') # tuple
r = range(9) #range
myDict = {"name": 'Hassan',  "age": 31} # dict
mySet = {'apple','banana','cherry'} # set
t = True # bool
b = b'hello' # bytes


print(s,i,f,c,myList,myTuple,mySet,myDict,t,b)

# Getting Data type - we use type()
print('Types =>',type(s),type(c),type(myTuple),type(t),type(b))

# Type Conversion
cif = float(i) 
cfi = int(f) 
cic = complex(i)
print(cif,cfi,cic)
print(type(cic)) 

# Random Numbers
import random 
print(random.randrange(1,20))

# Casting
castedInt1 = int(1)
castedInt2 = int(2.8)
castedInt3 = int('3')
castedFloat1 = float(1)
castedFloat2 = float(2.8)
castedFloat3 = float('3')
castedstring1 = str('s1')
castedstring2 = str(1)
castedstring3 = str(1.123)
print(castedInt2,castedFloat3,castedstring3)

# Strings => 'string' is the same as "string"
print("He's called 'Hassan'")
print('He\'s called "Hassan"') #escape character added \'
multilineString = """Demand is desire backed up by ability
to pay for goods in a specified period
"""
print(multilineString)
# strings are arrays
print(multilineString[3])

# loop thru string
for x in 'posh':
    print( x)
# length of a string
print(len(multilineString))
# check a string
txt = 'this msg is 4 you'
print('you' in txt) # gives a boolean accordingly
print('you' not in txt) # gives a boolean accordingly
# slicing strings
string1 = 'subah wanagsaan'
print(string1[3:8])
print(string1[:5]) # slice from start to pos 5
print(string1[6:]) # slice from pos 6 to the end
print(string1[-2]) # negative slicing starts from the end of the string
# modify strings
string1 = ' subah wanagsaan '
print(string1.upper())
print(string1.lower())
print(string1.strip()) # removes whitespace from start and end
print(string1.replace('u', 'a'))
print(string1.split(' ')) # splits the string into substrings if it finds instances of a separator
# string concatenation 
string2 = 'Students'
print(string1 + string2)
#format strings
price = 59
txt = f"The price is {price} dollars" #use f-string a a placeholder
print(txt)

# Booleans => represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)
# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# The rest return true e.g
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

   # operators
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y
# x -= 3	x = x - 3	
# x *= 3	x = x * 3
#comparison operators
# Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y
#logical operators 
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)