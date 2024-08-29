import re # built-in package for regular expressions
# A regular expression or regex is a sequence of characters that forms a search pattern
txt = 'No gaining in  ai without pain'
x = re.search('^No.*pain$', txt)

if x:
    print('Yes!!!, there is a match')
else:
    print('Sorry, no match.')    
# findall() function
y = re.findall("ai",txt) 
print(y) # list of matches
print(re.findall("ml",txt)) # no result, empty list

# the search() function
z = re.search('N',txt)
print(z.start()) # returns the position of the the match