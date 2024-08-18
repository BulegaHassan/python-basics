# order of execution
print('line1')
print('line2')
print('line3')

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


