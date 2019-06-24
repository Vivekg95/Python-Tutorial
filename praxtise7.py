s="good is better"
print(s.upper())
g="Durga Software Solution"
print(g.lower())
print(g.swapcase())
print(g.title())
print("the charcatre is {} and boy is {}".format(s,g))
print("".join(reversed(g)))
print(s[::-1])
i=len(g)-1 #14-1=13
target=""
while i>=0:
    target=target+g[i]
    i=i-1
print(target)
#FORMATTING DATE VALUES
import datetime
date=datetime.datetime.now()
print("It's now:{:%D/%M/%Y %H:%M:%S}".format(date))
complex=10+24j
print("Real part is {0.real} and imaginary part is {0.imag}".format(complex))
