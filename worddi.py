
b={'uyt':90,'tri':76,'ijt':98,}
a={'tat':920,'lki':746,'ik':56,}
print(a['tat'])
#print(b)
print(b['uyt'])
#c=dict (a.items() + b.items())
#print(c)
a.update({'srah':7609})
print(a)
del a['sarah']
print(a)
a.update(b)
print("Concatenated dictionary is:")
print(a)


