def main():
    count=0
    a=int(input("enter a number:"))
    for i in range(2,a):
        if(a%i)==0:
            count+=1
    if(count==2):
        print(a,"number is prime")

    else:
        print(a,"number is not prime")

if __name__=="__main__":main()

