def main():
    reverse=0
    a=int(input("Enter a number:"))
    for i in range(4):
    
        rem=(a%10)
        q=int(a/10)
        a=q
        reverse=reverse*10+rem
        print(reverse)
        
    if (reverse==a):
            print(a,"is palindrome")
    else:
            print(a,"is not palindrome")

    

    
    
    

        
        

    
    
    
    
        

if __name__=="__main__":main()