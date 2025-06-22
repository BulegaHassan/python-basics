print('-----------')
print('TUPLES')
print('-----------')
# A Tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.ordered, unchangeable, and allow duplicate values. Tuple items are indexed
thistuple = ("apple", "banana", "cherry", "apple", "cherry","orange", "kiwi", "melon", "mango")
print(thistuple,len(thistuple),type(thistuple))
tuple1 = ("abc", 34, True, 40, "male") # a tuple can contain different data types
tuple2 = tuple(("apple", "banana", "cherry")) # a tuple created with a tuple() constructor
print(thistuple[2:5]) # a tuple can be indexed from single indexes to ranges. Negative indexes can also be used

# Tuples are unchangeable, or immutable => But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = (1,2,3,19)
print(x)
y = list(x)
y[0] =5 # change
y.append(7) # add 
y.remove(19) # remove
x = tuple(y)
print(x)
# to add a tuple to a tuple
z = (11,)
x += z
print(x)
# del entire tuple => del thistuple

# Unpacking a tuple: => extracting values into variables

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print('........\n')
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)

# Loop thru a tuple => SIMILAR TO LOOPING THRU A LIST, SEE LINES 34-45

# join tuples using the '+' operator
