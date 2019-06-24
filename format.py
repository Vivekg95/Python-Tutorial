def main():
    a=int(input("enter a number:"))
    
    
    for i in range(2,a):
        if(a%i)==0:
            print(a,"number is  not prime")
            break
                
    else:
        print(a,"is prime ")
            
        
    

if __name__=="__main__":main()
    
