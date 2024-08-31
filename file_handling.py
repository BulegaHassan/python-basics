# python has several functions for making CRUD operations on files
# 'r'(default)- opens file for reading,  'a'- opens file for appending,  'w'- opens file for writing,  'x'- creates a specified file
# the above operations return errors if file doesnot exist except for 'w'
#  in addition you can specify if the file should be handled as binary-'b' 0r text-'t'(default)

# f = open('demofile.txt') # same as f = open('demofile.txt', 'rt')  file does not exist
#  read file
f = open('demofile2.txt')
print(f.read())
print('--------\n')

# open on different location
women = open(r"C:\Users\hassan\Desktop\notepad\women.txt", "r")
print(women.read())
women.close() #close file

print('--------\n')

# read some parts of file
f = open('demofile2.txt')
print(f.read(15))
print('--------\n')

# read lines
print(f.readline())

print('\n----------------\n')
#  write to an existing file
# "a" will append to the end of the file WHILE "w" overwrites existing file
f = open('demofile2.txt','a')
f.write('The forth line is added!')
f.close()
# open and read file after appending
f = open('demofile2.txt','r')
print(f.read())
print('\n----------------\n')

# overwrite file
f3 = open('demofile3.txt','w')
f3.write('Former content kaput! new content is ...')
f3.close()
# open and read file after overwriting
f3 = open('demofile3.txt','r')
print(f3.read())