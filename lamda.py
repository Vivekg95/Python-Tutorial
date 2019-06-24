sum=lambda arg1,arg2 : arg1+arg2
sub=lambda arg1,arg2 : arg1-arg2
mul=lambda arg1,arg2 : arg1*arg2
div=lambda arg1,arg2 : arg1/arg2

arg1=int(input("Enter a number:"))
arg2=int(input("Enter another number"))

res1=sum(arg1,arg2) #always assign variable to sum i.e res1 or another
res2=sub(arg1,arg2)
res3=mul(arg1,arg2)
res4=div(arg1,arg2)

print(res1)
print(res2)
print(res3)
print(res4)



