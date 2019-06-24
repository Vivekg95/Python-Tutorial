def add(a,b):
    result1=a+b
    print("Sum of two number is{}".format(result1))
    return result1
    


def sub(a,b):
    result2=a-b
    return result2

def mul(a,b):
    result3=a*b
    return result3




def main():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    result1=add(a,b)
    print(result1)
    result2=sub(a,b)
    print(result2)
    result3=mul(a,b)
    print(result3)

if __name__=="__main__":main()