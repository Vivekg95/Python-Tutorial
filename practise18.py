def main():
    f=open("C:\\Users\\Vivek Kumar\\Desktop\\python10\\guru99.txt","w+")
    for i in range(10):
        f.write("this is line %d\r\n" % (i+1))
    f.close()
if __name__ == "__main__":main()
    

