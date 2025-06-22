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
