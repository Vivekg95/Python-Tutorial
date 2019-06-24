class Car:
    def __init__(self,**ram):
        self.data=ram

def main():
    obj=Car(name="vivek",model="xyz")
    print(obj.data["name"])



if __name__=="__main__":main()

