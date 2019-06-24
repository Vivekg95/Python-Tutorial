class User:
    name = ""
    
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name  = " + self.name)

class Programmer(User):
    def __init__(self, name):
        self.name = name

    def doPython(self):
            print("Programming Python")

brian = User("brian")
brian.printName()

diana = Programmer("Diana")
diana.printName()
diana.doPython()
"""Name  = brian
Name  = Diana
Programming Python"""#output

class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
        
    class Head:
        def talk(self):
            return 'talking...'
        
if __name__ == '__main__':
    guido = Human()
    print (guido.name)
    print (guido.head.talk())
