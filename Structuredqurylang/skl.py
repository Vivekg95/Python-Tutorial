import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="708312@vk",database="College")
mycursor=mydb.cursor()
#mycursor.execute("show databases")
mycursor.execute("select * from Base")
for i in mycursor:
    print(i)
