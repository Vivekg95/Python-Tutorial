def main():
    count=0
    
    a=int(input("Enter anumber:"))
    for i in range(1,a+1):
        if(a%i)==0:
            count+=1
    if (count==2):
        print(a,"is prime")
                
    else:
        print(a,"is not prime")
                
            





if __name__=="__main__":main()

