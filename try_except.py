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
# finally block
print('--------\n')
try:
  print(x) # x is not defined
except:
  print('Something  wrong happened')
finally:
  print('the "try except" is finished')
print('--------\n')
#  try opening a non existing file
try:
  f = open('demofile.txt')
  try:
    f.write('lorem ipsum')
  except:
    print('Something  wrong happened when writing to the file')
  finally: 
    f.close()
except:
  print('Something  went wrong when opening the file')

print('--------\n')


#  You can thow an exception using the raise keyword
x = -1 
if x < 0:
  raise Exception('sorry, negative numbers not allowed')


  