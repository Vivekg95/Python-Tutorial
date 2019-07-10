import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="708312@vk",database="motog3")
mycursor=mydb.cursor()

#mycursor.execute("CREATE DATABASE Motog3")
#mycursor.execute("CREATE TABLE motog4(reg VARCHAR(20),user VARCHAR(20))")
"""sql = "INSERT INTO motog4(reg, user) VALUES (%s, %s)"
val=("vitt","vvirek")"""
mycursor.execute("SELECT * FROM motog4")

myresult = mycursor.fetchall()
print(myresult)

"""for x in myresult:
  print(x)"""
