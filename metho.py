class M:
    def add(self):
        a=int(input("enter something:"))
        print(a)
class N:
    def add(self,b):
        b=int(input("enter numbers:"))
        print(b)
class O(M,N):
    def mul(self,c):
        c=int(input("enter no:"))
        print(c)

def main():
    obj=M()
    obj.add()
    obj=N()
    obj.add("rt")
    obj=O()
    obj.mul("raj")
  

   
#we can write print in main
    
    
if __name__=="__main__":main()
