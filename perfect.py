
def main():
    a=int(input("enter a number:"))
    i=1
    
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
    if(sum==a):
        print("perfect")
    else:
        print("not perefect")        
 

if __name__=="__main__":main()

