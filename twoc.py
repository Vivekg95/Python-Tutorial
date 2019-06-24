class One:
    def add(self):
        a=int(input("enter something:"))
        print(a)
class Two:
    def sub(self):
        b=int(input("enter no:"))
        print(b)
def main():
    obj=One()
    obj.add()    #we can write print in main
    obj=Two()
    
    
    
    obj.sub()
    
if __name__=="__main__":main()
