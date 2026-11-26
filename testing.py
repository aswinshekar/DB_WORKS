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



while(1):
    print("1.INSERT\n2.READ\n3.SEARCH\n4.UPDATE\n5.DELETE\n6.EXIT")
    ch=int(input("ENTER YOUR CHOICE: "))
    if ch==1:
        pass
    elif ch==2:
        pass
    elif ch==3:
        pass
    elif ch==4:
        pass
    elif ch==5:
        pass
    elif ch==6:
        pass