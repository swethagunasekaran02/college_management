import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Swetha@09",
        database="worker_info"
    )
def insertfun():
    mydb = get_connection()
    cursor=mydb.cursor()
    cursor = mydb.cursor()
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    query = "INSERT INTO detail (name, age, address) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, address))
    mydb.commit()
    print("Inserted successfully.")
    cursor.close()
    mydb.close()

def selectAll():
    mydb = get_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM detail"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    cursor.close()
    mydb.close()

def delete():
    mydb = get_connection()
    cursor = mydb.cursor()
    rno = int(input("Enter the ID to delete: "))
    query = "DELETE FROM detail WHERE id = %s"
    cursor.execute(query, (rno,))
    mydb.commit()
    print("Deleted successfully.")
    cursor.close()
    mydb.close()

def update():
    mydb = get_connection()
    cursor = mydb.cursor()
    rno = int(input("Enter the ID to update: "))
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    address = input("Enter new address: ")
    query = "UPDATE detail SET name = %s, age = %s, address = %s WHERE id = %s"
    cursor.execute(query, (name, age, address, rno))
    mydb.commit()
    print("Updated successfully.")
    cursor.close()
    mydb.close()

def show():
    mydb = get_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM detail WHERE address = 'chennai'"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    mydb.close()

# Menu loop
isvalid = True

while isvalid:
    print("\n1. Insert\n2. Select All\n3. Delete\n4. Update\n5. Show Chennai\n6. Exit")
    choice = input("Enter a number: ")
    
    if choice == '1':
        insertfun()
    elif choice == '2':
        selectAll()
    elif choice == '3':
        delete()
    elif choice == '4':
        update()
    elif choice == '5':
        show()
    elif choice == '6':
        isvalid = False
    else:
        print("Invalid choice. Try again.")
