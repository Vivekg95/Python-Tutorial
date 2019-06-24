import re
f1=open("C:\\Users\\Vivek Kumar\\Desktop\\python10\\input.txt","r")
f2=open("C:\\Users\\Vivek Kumar\\Desktop\\python10\\output.txt","w")
for line in f1:
    list=re.findall("[7-9]\d{9}",line)
    for n in list:
        f2.write(n+"\n")
print("extract all no into output.txt")
f1.close()
f2.close()
