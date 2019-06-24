
class Car(object):

    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()

    factory = staticmethod(factory)#A method you can call without instantiating a class

class Racecar(Car):
    def drive(self):
        print("Racecar driving.")  #factory nd inheritance

class Van(Car):
    def drive(self):
        print("Van driving.")

# Create object using factory.
obj = Car.factory("Racecar")
obj.drive()