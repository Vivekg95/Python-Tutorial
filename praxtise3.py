def main():
#if else
    a=4
    b=5
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
    #if elif else
    name=input("enter name:")
    if(name=="vivek"):
        print("hello Vivek")
    elif(name=="sanu"):
        print("Sanu good boy")
    elif(name=="subham"):
        print("sing a song")
    else:
        print("Go enjoy Yourselves")
    num1=input("enter first num:")
    num2=input("enter second number:")
    num3=input("enter third number:")
    if(num1>num2 and num1>num3):
        print("num1 is greater")
    elif(num2>num3):
        print("num2 is greater")
    else:
        print("num3 is greater")
    #check no is even or not
    number=int(input("enter a number"))
    
    if(number%2==0):
        print("no is even")
    else:
        print("no is odd")
    numbers=int(input("enter nos.:"))
    if(numbers>=1 and numbers<=100):
        print(numbers,"is in between")
        
    else:
        print("Did I asked this?",numbers)

if __name__ == "__main__":main()

