import mysql.connector
class Person:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user="root",password="Root",host="localhost",database="person_db")
            print("CONNECTION SUCCESFULL")
        except:
            print("FAILED TO CONNECT")
    def create(self,id,name,age):
        c=self.con.cursor()
        query="insert into person (id,name,age) values(%s,%s,%s)"
        data=(id,name,age)
        c.execute(query,data)
        self.con.commit()
        print("RECORD INSERTED ")
    d
p=Person()
while(1):
    print("1.create\n2.read\n3.retrive\n4.update\n5.delete\n6.exit")
    ch=int(input("ENTER YOUR CHOICE: "))
    if ch==1:
        i=int(input("ENTER ID: "))
        n=input("ENTER NAME: ")
        a=int(input("ENTER AGE: "))
        p.create(i,n,a)


    elif ch==2:
        pass
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        pass
    elif ch == 6:
        pass
