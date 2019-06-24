def main(): #for demonstrating exception
    
    try:
        
    
        file=open("C:\\Users\\Vivek Kumar\\Desktop\\python10\\read1.txt", "r")
        print(file.read(1))
        print(file.read(2))
        file.close()
    except FileNotFoundError: #except Filenotfound as e:
        print("File not found") #we have to write a print statement after exception black 
        #print(e,file=stderr)
        

       

if __name__=="__main__":main()