# DEFINE A CLASS TO PERFORM DATABASE OPERATIONS ON VEHICLE TABLE
# CREATE A CLASS NAMED VehicleListCreateRetriveUpdateDelete
# AND DEFINE METHODS
# LIST()-- READING ALL RECORDS
# CREATE()--FOR CREATING A NEW RECORD
# RETRIVE(ID)--FOR READING A SPECIFIC RECORD
# UPDATE(ID,DATA)-- FOR UPDATING A SPECIFIC RECORD
# DELETE(ID)-- FOR DELETEING A SPECIFIC RECORD


import mysql.connector

class VehicleListCreateRetriveUpdateDelete:
    def __init__(self):
        # TO SET A COMMON CONNECTION
        # WHEN THE OBJECT OF THIS CLASS IS CREATED THE
        # CONNECTION IS ESTABLISHED
        self.connection=mysql.connector.connect(user="root",password="Root",host="localhost",database="vehicle")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("SUCCESSFULLY CONNECTED")

    def list(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
                print(records)
        else:
            print("NO RECORD FOUND")


    def create(self,brand,model,type,price,year):
        query="insert into book(brand,model,type,price,year) values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("DATA INSERTED SUCESSFULLY")



    def retrive(self,id):
        query="select * from vehicle where id = %s "
        data=(id,)
        self.cursor.execute(query,data)
        records = self.cursor.fetchall()
        if records:
            print(records)
        else:
            print("NO RECORD FOUND")




    def update(self,title,author,price,page,language,id):
        query="update book set title=%s, author=%s,price=%s,page=%s,language=%s where id =%s"
        data=(title,author,price,page,language,id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("UPDATE SUCCESFULLY ")
        else:
            print("NO RECORD FOUND")


    def delete(self,id):
        query = "delete from book where id = %s "
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("DELETED")
        else:
            print("NO RECORD FOUND")