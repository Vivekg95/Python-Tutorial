def main():
    try:
        #res=2/0
        file=open("C:\\Users\\Vivek Kumar\\Desktop\\python10\\read2.txt", "r")
        #list=["vk","rah","goa","rahul"]
        print(file.read(1))
        file.close()
        #print(res)
        #print(list[4])
    except FileNotFoundError:
        print("File not found here")
        list=["vk","raj","ram"]
        print(list[2])
    except IndexError:
        print("Array out of index")
if __name__=="__main__":main()