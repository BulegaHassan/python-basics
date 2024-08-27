# Consider a module to be the same as  a code library. Its a file containing functions you   may want to use in your app.
import mymodule
import mymodule as mm # renaming a module
import platform 

mymodule.greeting('Hassan')

c = mymodule.person1['country']
print(c)
a = mm.person1['age']
print(a)

p = platform.system()
print(p)