filename="C:\\Users\\Vivek Kumar\\Desktop\\python10\\fforensic.txt"
contenet=open(filename,'a')
n=input("enter something")
contenet.write(n)
contenet.close()
"""r	Open file for reading
w	Open file for writing (will truncate file)
b	binary more
r+	open file for reading and writing
a+	open file for reading and writing (appends to end)
w+	open file for reading and writing (truncates files)"""