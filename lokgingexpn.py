import logging
logging.basicConfig(filename='C:\\Users\\Vivek Kumar\\Desktop\\python10\\mylog.txt',level=logging.INFO)
logging.info("A new request came")
try:
    x=int(input("enter number"))
    y=int(input("enter anoter number"))
    print(x/y)
except ZeroDivisionError as msg:
    print("Cannot divide by zero")
    logging.exception(msg)
except ValueError as msg:
    print("give only int ")
    logging.exception(msg)
logging.info("completed")