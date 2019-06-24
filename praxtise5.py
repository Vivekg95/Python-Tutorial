def main():
    n=int(input("enter the no of rows:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
    for x in range(1,n+1):
        print("*"*x)

if __name__ == "__main__":main()
    