class Word:
    def alp(self):
        try:
            a=input("Enter something:")

                                            #print(type(a))
            print(type(a))
            if a.isdigit():
            
            #if(type(a)==int):               #a.isdigit():
                print("a is number") 
            else:
    
                print("a is alphabet")
        except Exception:
            print("not a digit")
                
def main():
    obj=Word()
    obj.alp()

if __name__=="__main__":main()
        