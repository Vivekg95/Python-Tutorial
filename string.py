"""a=input("enter something:")
n=0
sum=0
while(a>0):
    n=a%10
    sum=sum*10+n
    a=a//10
print(sum)"""

"""a="good"
print(a[::-1])"""
seqString = 'Python'
print(list(reversed(seqString)))

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))
def viv(x):
    return x[::-1]
mytest=viv("how are you")
print(mytest)
"""def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))
"""