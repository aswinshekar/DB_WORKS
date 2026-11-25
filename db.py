while(1):
    print(" 1. INSERT PRODUCT DETAILS\n2. READ ALL PRODUCT DETAILS\n3. SEARCH A PRODUCT BY PRODUCT_ID"
        "\n4. UPDATE THE STOCK OF A PRODUCT\n5. DELETE A PRODUCT RECORD\n6. EXIT")
    op=int(input("ENTER Y0UR CHOICE: "))
    if op==1:
        insert()
    elif op==2:
        read()
    elif op==3:
        search()
    elif op==4:
        update()
    elif op==5:
        delete()
    elif op==6:
        exit()
