class M:
    def add(self):
        a=int(input("enter something:"))
        print(a)
class N(M):
    def sub(self,b):
        b=int(input("enter numbers:"))
        print(b)
class O(N):
    def mul(self,c):
        c=int(input("enter no:"))
        print(c)

def main():
    obj=O()
    obj.mul("raj")
    obj.sub("rt")
    obj.add()
    

   
#we can write print in main
    
    
if __name__=="__main__":main()
