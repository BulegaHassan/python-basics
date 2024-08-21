# 4 built-in data types in Python are used to store Collections of data -List, Tuple, Set, and Dictionary.
print('-----------')
print('LISTS')
print('-----------')
#LISTS - are created using square brackets
#  List items are indexed, ordered, changeable, and allow duplicate values. 
thislist = ["apple", "banana", "cherry"]
print(thislist,'has length of ',len(thislist), ' of type ', type(thislist))
# List can contain different data types
list1 = ["abc", 34, True, 40, "male"]
# We can use a list() constructor to make a List:
thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(thislist)
# Accessing lists 
print(thislist[1], thislist[-1], thislist[2:5],"apple" in thislist) 
# Changing list items
thislist[1] = 'blackcurrant'
thislist[1:3] = ["blackcurrant", "watermelon"]
thislist.insert(2, "watermelon")
print(thislist)
# Add list items
thislist.append("dates")
print(thislist)
tropical = ["mango", "pineapple", "papaya", "banana"]
thislist.extend(tropical) # the extend method can add any iterable object (tuples, sets, dictionaries etc.)
print(thislist)
# Remove list items
thislist.remove("banana")
thislist.pop(4) # removes at the specified index, if no index is specified it removes the last item
del thislist[0] # removes at the specified index, can also delete the entire list ie del thisList
print(thislist)
thislist.clear() # empties the list
print(thislist)
# Loop thru a list
thislist = ["apple", "banana", "cherry"]
for x in thislist: #for loop
  print(x)
print('-------')
for i in range(len(thislist)): # loop using indexes
  print(thislist[i])
print('-------')
i = 0 # using a while loop
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print('-------')
[print(x) for x in thislist] # loop using list comprehension

# List comprehension - offers shorter syntax
fruits = ["orange", "mango", "kiwi", "cherry","pineapple", "banana"] # we want a new list, containing only the fruits with the letter "a" in the name.
newlist = [x for x in fruits if "a" in x]
print(newlist)
# Sort List
fruits.sort() # sort alphabetically
thislist = [100, 50, 65, 82, 23]
thislist.sort() # sort numerically
print(fruits,thislist)
fruits.sort(reverse = True) # sort descending
thislist.sort(reverse = True) # sort descending
print(fruits,thislist)
hisList = ["banana", "Orange", "Kiwi", "cherry"]
hisList.sort(key = str.lower) # case-insensitive sort function
print(hisList)
# copy lists
thislist = ["apple", "banana", "cherry"]
mylist1 = thislist.copy() # make a copy of a list
mylist2 = list(thislist) # use the list() method
mylist3 = thislist[:] # use the slice operator
print(mylist1,mylist2,mylist3)
# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
list1.extend(list2) # use the extend() method to add list2 at the end of list1
print(list3,list1)

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

print('-----------')
print('SETS')
print('-----------')
# A set is a collection which is unordered, unchangeable*, and unindexed, Duplicates Not Allowed. Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry", "apple", 1, True,2, 0, False} # 1 and True are considered the same

print(thisset,len(thisset), type(thisset))
thisset1 = set(("apple", "banana", "cherry")) # using a set constructor
# access set members
for x in thisset: #using a for loop
  print(x)

print("banana" in thisset) # check if member is present
# Add set members
thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # add set items from another-set(or any other iterable) into the current set
print(thisset)
# remove set items
thisset.remove("banana")
thisset.discard("cherry")
thisset.pop() # removes a random value
# thisset.clear()  empties the set
# del thisset  deletes the set completely
print(thisset)
# You can loop through the set items by using a for loop:
for x in thisset:
  print(x)

# Join sets
# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set3 = set1 | set2 # same as union()
print(set3) # For multiple sets then set1.union(set2,set3,...,setn) or set1 | set2 | set3 | ... | setn

# Intersection => Keeps ONLY the duplicates 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set3 = set1 & set2 # same as intersection()
print(set3)
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# set1.intersection_update(set2)

# print(set1)
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set3 = set1.difference(set2)

print(set3)