#x=range(1,6)
lis1 = list(range(6)) 
print(lis1)
print("hello")
print(list(range(1,10,2)))
least=[1,"asc",56]
least.append(5894)
print(least)#If you want to assign multiple variables at once, you can use tuples:

#TUPLE
x=(1,2,"qwd")


print(x)
#convert tuple to list
y=list(x)
print(y)
#convert list to tuple
z=tuple(least)
print(z)
#If you want to assign multiple variables at once, you can use tuples:
name,no,country=("ramayanasa",45,"india")
print(name)

person = ("Diana","Canada","CompSci" ) #Diana-trial ,Canada-trial ,CompSci
s = "-trial ,".join(person)#here compsci doesnot get add with trial
print(s)

#below are correct code

s = ""
person = ('Diana', 'Canada', 'CompSci' )
"""men="-trial"
print(men.join(person))"""
for i in range (len(person)):
    s = s + person[i] + "-trial "
print (s)
"""Lists are dynamic in size while tuples are fixed. 
   You can’t add or remove elements to a tuple.
   Tuples are faster than lists. They secure from data being modified.
   If you have an existing tuple, you can append to it with the + operator.  
   You can only append a tuple to an existing tuple."""
dict = {}
dict['Ford'] = "Car"
dict['Python'] = "The Python Programming Language"
dict[2] = "This sentence is stored here."

print(dict['Ford'])
print(dict['Python'])
print(dict[2])
print(dict)

vk=2.5
print(type(vk))
#random module
from random import *

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(items)
print(randint(1,10))

xb = sample(items,  1)   # Pick a random item from the list
print(xb[0])

yb = sample(items, 4)    # Pick 4 random items from the list
print(yb)

print(items)



