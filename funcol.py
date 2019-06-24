class Overloading:
    
    def sum(self):
        a=int(input("enter first no:"))
        b=int(input("enter second no:"))         #
        add=a+b
        print(add)
    
    def sub(self):
        a=int(input("enter first no:"))
        b=int(input("enter second no:"))  
        c=int(input("enter a number:"))       #
        add=a+b+c
        print(add)



       
            
def main():
    obj=Overloading()
    obj.sum()
    obj.sub()
    

if __name__=="__main__":main()


