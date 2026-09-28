# DEFINE A CLASS TO PERFORM DATABASE OPERATIONS ON BOOK TABLE
# CREATE A CLASS NAMED BookListCreateRetriveUpdateDelete
# AND DEFINE METHODS
# LIST()-- READING ALL RECORDS
# CREATE()--FOR CREATING A NEW RECORD
# RETRIVE(ID)--FOR READING A SPECIFIC RECORD
# UPDATE(ID,DATA)-- FOR UPDATING A SPECIFIC RECORD
# DELETE(ID)-- FOR DELETEING A SPECIFIC RECORD


import mysql.connector

class BookListCreateRetriveUpdateDelete:
    def __init__(self):
        # TO SET A COMMON CONNECTION
        # WHEN THE OBJECT OF THIS CLASS IS CREATED THE
        # CONNECTION IS ESTABLISHED
        self.connection=mysql.connector.connect(user="root",password="Root",host="localhost",database="Library_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("SUCCESSFULLY CONNECTED")
    def list(self):
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
                print(records)
        else:
            print("NO RECORD FOUND")


    def create(self,title,author,price,page,language):
        query="insert into book(title,author,price,page,language) values(%s,%s,%s,%s,%s)"
        data=(title,author,price,page,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("DATA INSERTED SUCESSFULLY")


    def retrive(self,id):
        query="select * from book where id = %s "
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
            
book_instance=BookListCreateRetriveUpdateDelete()
# book_instance.list()
# book_instance.create(title="SHA",author="AMAL",price=100,page=380,language="ENGLISH"
# book_instance.retrive(2)
book_instance.update("HELLO","BLESSON",30,10,"MALAYALAM",2,)
# book_instance.delete(2)

