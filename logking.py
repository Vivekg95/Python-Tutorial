import logging
logging.basicConfig(filename='C:\\Users\\Vivek Kumar\\Desktop\\python10\\log.txt',level=logging.WARNING)
#logging.DEBUG will give full message unlike WARNING
print("logging demo")
logging.debug("this is good")
logging.info("info message")
logging.warning("this warning")
logging.critical("critical mesaage")
