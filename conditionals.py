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
