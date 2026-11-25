import mysql.connector
class Person_db:
    def __int__(self):
        try:
            self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="person_db")
            print(self.con)
        except:
            print("Failed to connect")
    def create(self,id,name,age):
        pass
    def read(self):




while(1):
    print(" 1. create")
    print(" 2. read")
    print(" 3. retrive")
    print(" 4. update")
    print(" 5. delete")
    print(" 6. exit")

    op=int(input("ENTER Y0UR CHOICE: "))

    if op==1:
        # insert()
    elif op==2:
        # read()
    elif op==3:
        # search()
    elif op==4:
        # update()
    elif op==5:
        # delete()
    elif op==6:
        exit()
