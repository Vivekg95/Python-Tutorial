class Calculator:    
    
    
                   #a=int(input("Enter First number:"))
                                    #b=int(input("Enter another number:"))
    def add(self):
        a=int(input("Enter First number:"))
        b=int(input("Enter another number:"))
        return a+b
       
    def sub(self):
        a=int(input("Enter First number:"))
        b=int(input("Enter another number:"))
        return a-b

        
    def mul(self):
        a=int(input("Enter First number:"))
        b=int(input("Enter another number:"))
        return a*b
    choice=int(input("enter choice:"))
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    if choice == "1":   
        print(add)
    if choice == "2":
        print(sub)
    if choice=="3":
        print(mul)
    
    


def main():
  
    obj=Calculator()
    obj.add()
    obj.sub()
    obj.mul()
    
   
if __name__=="__main__":main()