# 4 built-in data types in Python are used to store Collections of data -List, Tuple, Set, and Dictionary.

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