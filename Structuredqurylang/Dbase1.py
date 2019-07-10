import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="708312@vk",database="mydatabase")
#print(mydb)
mycursor=mydb.cursor()
sql="INSERT INTO Mobile(mobno,name) VALUES(%s, %s)"
val=[("7083122952","VIVEK"),("789654212","RAMHARi")]

mycursor.executemany(sql,val)
mydb.commit()
#mycursor.executemany("SHOW TABLES")

"""for x in mycursor:
    print(x)"""