n=int(input("enter no of students:"))
d={}
for i in range(n):
    marks=int(input("enter student's marks:"))
    name=input("enter name of students:")
    d[name]=marks
    #print(d)
while True:
    name=input("enter student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("student not found")
    else:
        print("marks of",name,"are",marks)
    option=input("Do you want to get another student marks[Y][N]")
    if option=="N":
        break
print("Thamks for is our application")