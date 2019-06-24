class Car:
    def brand(self,brandtype):
        print(brandtype)
    def model(self,modeltype):
        print(modeltype)




def main(brand,model):
    obj=Car()
    obj.brand(brand)
    obj.model(model)
    
if __name__=="__main__":main("TATA NANo","XYZ")

