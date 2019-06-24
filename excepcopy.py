import sys

def main():
    try:
        
        file1=open("C:\\Users\\Vivek Kumar\\Desktop\\python10\\read1.txt", "r")#file not found error
        print(file1.read(1))
        file1.close()

        res=2/0 #divide by zer0
        print(res)
        list=["vk","rah","goa","rahul"]
        
        
        print(list[4]) #Index error#index out of range
    except (ZeroDivisionError,IndexError,FileNotFoundError):#use parenthesis 
        print("File not found") 
    
    
        
if __name__=="__main__":main()