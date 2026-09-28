# # Create a database named shop
# import mysql.connector
# # con=mysql.connector.connect(user="root",password="Root",host="localhost")
# # c=con.cursor()
# # c.execute("create database SHOP ")
# # print("DataBase file created")
#
# con=mysql.connector.connect(user="root",password="Root",host="localhost",database="SHOP")
# c=con.cursor()
# # c.execute('''
# # create table product(product_id int not null primary key,
# #                     name varchar(20),
# #                     brand varchar(20),
# #                     category varchar(20),
# #                     price varchar(20),
# #                     stock varchar(20))''')

# # c.execute('''
# # insert into product(product_id,name,brand,category,price,stock) values
# #
# #
# # ''')
#
# # Create a database named shop
# # Create a table `Product` with the following fields:
#
# #  `product_id` – Primary Key
# #  `name`
# #  `brand`
# #  `category`
# #  `price`
# #  `stock`

# # Write a menu-driven Python program using MySQL with the following options:
#
# # text
# # 1. Insert Product details
# # 2. Read all Product details
# # 3. Search a Product by product_id
# # 4. Update the stock of a Product
# # 5. Delete a Product record
# # 6. Exit
#
#
# def insert():
#     prd_id=int(input("ENTER THE PRODUCT_ID: "))
#     name=input("ENTER THE NAME: ")
#     brand=input("ENTER THE BRAND NAME:")
#     category= input("ENTER THE CATEGORY: ")
#     price=int(input("ENTER THE PRICE: "))
#     stock=int(input("ENTER THE STOCK:"))
#     query=" insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)"
#     data=(prd_id,name,brand,category,price,stock,)
#     c.execute(query,data)
#     con.commit()
#     print("INSERTED")
#
# def read():
#     query="select * from product"
#     c.execute(query)
#     content=c.fetchall()
#     if content:
#         print(content)
#     else:
#         print("NO CONTENTS")
# def search():
#     se=int(input("ENTER THE PRODUCT_ID TO SEARCH: "))
#     query="select * from product where product_id=%s"
#     data=(se,)
#     c.execute(query,data)
#     record=c.fetchall()
#     if record:
#         print(record)
#     else:
#         print("NO PRODUCT FOUND")
#
# def update():
#     proid=int(input("ENTER THE PRODUCT ID YOU WANT TO UPDATE:"))
#     up=input("ENTER THE UPDATED STOCK: ")
#     query="update product set stock=%s where product_id=%s"
#     data=(up,proid)
#     c.execute(query,data)
#     con.commit()
#     print("UPDATED ")
#
# def delete():
#     proid = int(input("ENTER THE PRODUCT ID YOU WANT TO DELETE:"))
#     query="delete from product where product_id=%s"
#     data=(proid,)
#     c.execute(query,data)
#     con.commit()
#     print("DELETED")
# while(1):
#     print(" 1. INSERT PRODUCT DETAILS\n2. READ ALL PRODUCT DETAILS\n3. SEARCH A PRODUCT BY PRODUCT_ID"
#         "\n4. UPDATE THE STOCK OF A PRODUCT\n5. DELETE A PRODUCT RECORD\n6. EXIT")
#     op=int(input("ENTER Y0UR CHOICE: "))
#     if op==1:
#         insert()
#     elif op==2:
#         read()
#     elif op==3:
#         search()
#     elif op==4:
#         update()
#     elif op==5:
#         delete()
#     elif op==6:
#         exit()



