import sqlite3 as lite
import sys

con = lite.connect('C:\\sqllite\\user.db')

with con:
    
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2,'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3,'Greg')")
    cur.execute("INSERT INTO Users VALUES(4,'Grhggeg')")

    
    