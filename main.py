from controller import DatabaseManager

print("----------------------------")
print("Welcome to TC Contact Book")
print("----------------------------")
print("What do you want to do? ")
print("1. Add Contact")
print("2. List Contact")
print("3. Delete Contact")
print("4. Update Contact")
print("5. Search Contact")
print("6. List Single")
print("7. Exit")
print("----------------------------")

choice = int(input("Enter your choice: "))

# For DB
host = "localhost"
user = "root"
password = ""
database = "phonebook"

db_manager = DatabaseManager(host, user, password, database)

if choice == 1:
    print("Add Contact")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    db_manager.add_person(name, phone)
elif choice == 2:
    print("List Contact")
    db_manager.list_persons()
elif choice == 3:
    print("Delete Contact")
    id = input("Enter id: ")
    db_manager.delete_person(id)
elif choice == 4:
    print("Update Contact")
elif choice == 5:
    print("Search Contact")
elif choice == 6:
    print("List Single")
    id = input("Enter id: ")
    db_manager.list_by_id(id)
elif choice == 7:
    print("Exit")
else:
    print("Invalid choice")
