# The try block lets you test a block of code for errors, the except block lets you handle the error, the else block lets you execute code when there is no error. The finally block executes regardless of the result of the try- and except blocks
try:
  print(x) # x is not defined
except:
  print('An eception has occured')

print('--------\n')
# Many exceptions
try:
  print(x) # x is not defined
except NameError:
  print('var x is undefined')
except:
  print('Something else wrong happened')

print('--------\n')
# else defines a block of code if no errors
try:
  print('Salaam')
except:
  print('Something  wrong happened')
else:
  print('Nothing wrong happened')
  
  