import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:, convert json to python
y = json.loads(x)

# the result is a Python dictionary:
print(y)

# Convert python to json
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_json = json.dumps(my_dict)
print(my_json)
print('........\n')
# Converting python objects of diff types e.g list,int,bool, e.t.c into JSON strings
print(json.dumps({'name': 'Ali', 'age': 30}))
print(json.dumps(['apples','dates']))
print(json.dumps(('apple','date')))
print(json.dumps('labaik'))
print(json.dumps(31))
print(json.dumps(11.890))
print(json.dumps(True))
print('........\n')
# Format results - indenting and ordering
print(json.dumps(my_dict,indent=4, sort_keys=True))