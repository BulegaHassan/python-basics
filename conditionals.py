# if statement 
print('--------------')
print('if statement')
print('-------------')
a, b = 339, 45
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("b is less than a")
# using shorthand if statement
if a > b: print("a is greater than b")
# using shorthand if... else
a , b = 6, 6.0
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
# using and, or & not  operators
a = 200
b = 33
c = 500
d = 1999
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")
if not a > d:
  print("a is NOT greater than d")
# nested if statements
x = 1
if x > 10:
  print('x is greater than 10')
  if x > 15:
   print('x is also greater than 15')
  else:
    print('but x is less than 15')
else:
  print('x is a single digit')
# pass statement - an if statement cannot be empty, if for some reason then use a pass statement to avoid error
if x > 0:
  pass

# while loops 
print('--------------')
print('while loops')
print('-------------')
# With the while loop we can execute a set of statements as long as a condition is true.
i = 0
while i <= 5:
  print(i) 
  i += 1

print('----') 

# break statement - stops the loop even when the condition is true
i = 1
while i <= 5:
  print(i) 
  if i == 3:
    break
  i += 1

print('----') 

# continue statement - we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# for loops 
print('--------------')
print('for loops')
print('-------------')
#  A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
fruits.append("dates") 
for x in fruits:
  print(x)

print('--------------')

# break statement - we can stop the loop before it has looped through all the items
for y in fruits:
  print(y)
  if y == 'banana':
    break
  
print('--------------')
  
for x in fruits:
  if x == "banana":
    break
  print(x)

print('--------------')

#  the continue statement -  we can stop the current iteration of the loop, and continue with the next:
for x in fruits:
  if x == 'banana':
    continue
  print(x)

print('--------------')

#    The range() Function
for x in range(6):
  print(x)

print('--------------')

for x in range(2, 30, 3): # starts with 2 up to 30(not inclusive) in steps of 3
  print(x)

print('--------------')

#  The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(2,6):
  print(x)
else:
  print("Finally finished!")

print('--------------')

# Nested Loops - The "inner loop" will be executed one time for each iteration of the "outer loop"
for x in range(7):
  for y in range(5,66,5):
    print(x,y)

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for p in {1,2,3}:
 pass