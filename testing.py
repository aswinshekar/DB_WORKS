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
import mysql.connector
class Shop:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="Root",host="localhost",database="shop")
        print("CONNECTED")
    def create(self,product,name,brand,category,price,stock):
        c=self.con.cursor()
        query="insert into product(product_id,name,brand,category,price,stock) values (%s,%s,%s,%s,%s,%s)"
        data=(product,name,brand,category,price,stock)
        c.execute(query,data)
        self.con.commit()
        print("INSERTED")
    def read(self):
        c=self.con.cursor()
        query="select * from product"
        c.execute(query)
        record=c.fetchall()
        if record:
            for i in record:
                print(i)
        else:
            print("NO DATA")
    def search(self,id):
        c=self.con.cursor()
        query="select * from product where product_id=%s"
        data=(id,)
        c.execute(query,data)
        record=c.fetchall()
        if record:
            for i in record:
                print(i)
        else:
            print("NO DATA")
    def update(self,id,s):
        c=self.con.cursor()
        query="update product set stock=%s where product_id=%s"
        data=(s,id)
        c.execute(query,data)
        self.con.commit()
        if c.rowcount>0:
            print("UPDATED")
        else:
            print("CANNOT FIND ID ")


s=Shop()
while(1):
    print("1.INSERT\n2.READ\n3.SEARCH\n4.UPDATE\n5.DELETE\n6.EXIT")
    ch=int(input("ENTER YOUR CHOICE: "))
    if ch==1:
        p=input("ENTER PRODUCT_ID: ")
        n=input("ENTER  NAME: ")
        b=input("ENTER BRAND: ")
        c=input("ENTER CATEGORY: ")
        pr=int(input("ENTER PRICE: "))
        st=int(input("ENTER STOCK: "))
        s.create(p,n,b,c,pr,st)

    elif ch==2:
        s.read()
    elif ch==3:
        i=int(input("ENTER ID: "))
        s.search(i)
    elif ch==4:
        i=int(input("ENTER PRODUCT ID: "))
        st=int(input("ENTER NEW STOCK: "))
        s.update(i,st)
    elif ch==5:
        pass
    elif ch==6:
        pass