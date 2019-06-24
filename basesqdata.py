import sqlite3
def main():
    db=sqlite3.connect("C:\\sqllite\\sample.db")
    db.row_factory=sqlite3.Row
    #db.execute("create table hello(name text,age int)")
    db.execute("insert into hello(name,age)values('shubham',26)")
    db.execute("insert into hello(name,age)values('raju',30)")
    a=input("name")
    b=int(input("age"))
    db.execute("insert into hello(name,age)values(?,?)",(a,b))
    db.commit()
    result=db.execute("select * from hello" )
    for temp in result:
        print("name:{},age:{}".format(temp["name"],temp["age"])) #connectivity of mongodb
        #insert data#delete data
        
    print(type(result))
    
    

if __name__=="__main__":main()