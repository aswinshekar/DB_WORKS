from xmlrpc.client import SERVER_ERROR

import mysql.connector


# con=mysql.connector.connect(user="root",password="Root",host="localhost")
# # ESTABLISH CONNECTION BETWEEN PYTHON CODE AND MYSQL SERVER_ERROR
# # IT RETURNS A CONNECTION OBJECT
#
# print(con)
#
# c=con.cursor() # CURSOR OBJECT USED TO EXECUTE SQL QUEIRES /COMMANDS
#
# # c.execute(command)
# # CREATE DATABASE FILE
# c.execute("create database school_db ")
# print("DataBase file created")


con=mysql.connector.connect(user="root",password="Root",host="localhost",database="school_db")
c=con.cursor()


# c.execute('''
# create table student(roll_no int not null primary key,
#                 name varchar(20),
#                 age int ,
#                 place varchar(20),
#                 phone varchar (20),
#                 total_mark int) ''')

# print("Table succefully created")
# c.execute(''' insert into student(roll_no,name,age,place,phone,total_mark)
#                     values(101,"ASWIN",21,"ALUVA","8590543533",179),
#                           (102,"ATHUL",22,"EKM","9495-33129",160),
#                           (103,"AMAL",25,"KOCHI","098764836",155),
#                           (104,"DIYA",22,"CHENNAI","6753764836",165),
#                           (105,"REENA",20,"PKD","9543764836",140)''')

# con.commit()#TO SAVE DATA PERMENANTLY
# print("SUCCEFULLY INSERTED")

# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
#
# data=(106,'kiran',12,'ekm','5678374829',140)
#
# c.execute(query,data)
# con.commit()


# READ OPERATION


# query="select * from student "
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("NO RECORDS")


# READ ALL ATTRIBUTES OF A STUDENT WITH ROLL NUMBER = ROLL NUMBER ENTERED BY USER
# n= int(input("ENTER THE ROLL NUMBER "))
# query="select * from student where roll_no = %s "
# data=(n,)
# c.execute(query,data)
# records=c.fetchone()
# if records:
#     for row in records:
#         print(row,end=" ")
# else:
#     print("NO RECORDS")

# UPDATE MARK OF A STUDENT WITH ROLL_NO= ROLL_NO ENTER BYE THE USER

# n=int(input("ENTER THE ROLL_NUMBER:" ))
# m=int(input("ENTER THE NEW MARK: " ))
# query="update student set total_mark= %s where roll_no=%s"
# data=(m,n,)
# c.execute(query,data)
# con.commit()



# query="select * from student where roll_no = %s "
# data=(n,)
# c.execute(query,data)
# records=c.fetchone()
# if records:
#     for row in records:
#         print(row,end=" ")
# else:
#     print("NO RECORDS")




# DELETE A RECORD A STUDENT WITH ROLL_NO= ROLL_NO ENTER BYE THE USER
#
# number=int(input("ENTER THE ROLL_NO: "))
# query="delete from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# con.commit()

#  CREATE A NEW RECORD ENTERED BY A USER

# roll_no=int(input("ENTER THE ROLL_NO: "))
# name=input("ENTER THE NAME: ")
# age=int(input("ENTER THE AGE: "))
# place=input("ENTER THE PLACE: ")
# phone=int(input("ENTER THE PHONE_NO: "))
# total_mark=int(input("ENTER THE TOTAL_MARK: "))
# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(roll_no,name,age,place,phone,total_mark,)
# c.execute(query,data)
# con.commit()
# print("INSERTED")