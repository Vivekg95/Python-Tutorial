def main():
    reverse=0
    a=int(input("enter a number:"))
    temp=a
    for i in range(3): #while(n>0):we should rather use while121
        rem=a%10
    
        reverse=reverse*10+rem
        a=a//10
    if(temp==reverse):
        print("number is palindrome")
    else:
        print("number is not palindrome")



if __name__=="__main__":main()