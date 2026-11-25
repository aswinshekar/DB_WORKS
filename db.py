
#     def update(self,id,name,age):
#         try:
#             c=self.con.cursor()
#             query="update person set name=%s,age=%s where id=%s"
#             data=(name,age,id)
#             c.execute(query,data)
#             self.con.cursor()
#             if c.rowcount>0:
#                 print('RECORD UPDATED SUCCESSFULLY')
#             else:
#                 print('ID NOT FOUND')
#         except:
#             print("FAILED TO UPDATE")
#     def delete(self,id):
#         try:
#             c=self.con.cursor()
#             query='delete from person where id=%s'
#             data=(id,)
#             c.execute(query,data)
#             self.con.commit()
#             if c.rowcount>0:
#                     print('RECORD DELETED SUCCESSFULLY')
#             else:
#                     print('ID NOT FOUND')
#         except:
#             print("FAILED TO DELETE")
# b=Person_db()
# while(1):
#     print('1.Create')
#     print('2.Read')
#     print('3.Retrieve')
#     print('4.Update')
#     print('5.Delete')
#     print('6.Exit')
#
#     ch=int(input("enter your choice:"))
#
#     if ch==1:
#         i=int(input("enter id:"))
#         n=input('enter name:')
#         a=int(input('enter age:'))
#         b.create(i,n,a)
#     elif ch==2:
#         b.read()
#     elif ch==3:
#         i=int(input('enter id:'))
#         b.retrieve(i)
#     elif ch==4:
#         id=int(input('enter id to update:'))
#         n = input('enter name:')
#         a = int(input('enter age:'))
#         b.update(id,n,a)
#     elif ch==5:
#         i = int(input('enter id:'))
#         b.delete(i)
#     elif ch==6:
#         exit()


import mysql.connector
class Person:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(user="root", password='Root', host='localhost', database='person_db')
            print("Connection")
        except:
            print("Failed to connect")

    def create(self,id,name,age):
        try:
            c=self.con.cursor()
            query="insert into person(id,name,age) values(%s,%s,%s)"
            data=(id,name,age)
            c.execute(query,data)
            self.con.commit()
            print("RECORD INSERTED")
        except Exception as e:
            print("FAILED TO INSERT:", e)
    def read(self):
        try:
            c=self.con.cursor()
            query="select * from person"
            c.execute(query)
            content=c.fetchall()
            if content:
                for i in content:
                    print(i)
            else:
                print("NO RECORD FOUND")
        except:
            print("Failed to read")

    def retrive(self,id):
        try:
            c=self.con.cursor()
            query="select * from person where id=%s"
            data=(id,)
            c.execute(query,data)
            content=c.fetchall()
            if content:
                for i in content:
                    print(i)
            else:
                print("NO RECORD FOUND")
        except:
            print("FAILED TO FOUND")
    def update(self,f,name,age):
        c=self.con.cursor()
        query="update person set name=%s,age=%s where id =%s"
        data=(name,age,f)
        c.execute(query,data)
        self.con.cursor()
        if c.rowcount > 0:
            print('RECORD UPDATED SUCCESSFULLY')
        else:
            print('ID NOT FOUND')

p=Person()
while(1):
    print("1.create\n2.read\n3.retrive\n4.update\n5.delete\n6.exit")
    ch=int(input("ENTER THE CHOICE: "))
    if ch==1:
        i=int(input("enter id: "))
        n=input("enter name: ")
        a=int(input("enter age: "))
        p.create(i,n,a)
    elif ch==2:
        p.read()
    elif ch == 3:
        i=int(input("ENTER ID:"))
        p.retrive(i)
    elif ch == 4:
        f=int(input("ENTER THE ID TO BE UPDATED: "))
        n = input("enter name: ")
        a = int(input("enter age: "))
        p.update(f,n,a)
    elif ch == 5:
        pass
    elif ch == 6:
        exit()
