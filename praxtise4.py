def main():
    a="sunny"
    for i in a:
        print(i)
    for i in range(5):
        print(a)
    for i in range(10,0,-1):
        print(i)
    #Sum in list
    list=[10,20,30]
    sum=0
    for i in list:
        sum=sum+i
    print("sum is",sum)

    #while loop
    n=1
    while(n<=10):
        print(n)
        n=n+1
#sum
    d=10
    sum1=0
    x=1
    while(x<=d):
        sum1=sum1+x
        x=x+1
    print("sum1 is ",sum1)

    #confirming name
    names=" "

    while(names !="vivek"):
        names=input("enter a name")
    print("Thanks for confirming")
    #Nested loop
    for i in range(4):
        for j in range(4):
            print("i=",i,"j=",j)


if __name__ =="__main__":main()