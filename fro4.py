class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def walk(self):

        print(self.name , "walks and sound like",self.sound)
    def talk(self):
        print(self.name ,"talks like",self.sound)
        
duck=Animal("horse","hynn")
duck.walk()
duck.talk()