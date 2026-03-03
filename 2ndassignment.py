users = []

while True:
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

  
    if choice == "1":
        if len(users) == 0:
            print("No users found.")
        else:
            print("\nUser List:")
            for i, user in enumerate(users):
                print(f"{i}. {user}")

   
    elif choice == "2":
        new_user = input("Enter new user name: ")
        users.append(new_user)
        print("User added successfully!")

    
    elif choice == "3":
        if len(users) == 0:
            print("No users to update.")
        else:
            for i, user in enumerate(users):
                print(f"{i}. {user}")
            index = int(input("Enter user number to update: "))
            if 0 <= index < len(users):
                updated_name = input("Enter new name: ")
                users[index] = updated_name
                print("User updated successfully!")
            else:
                print("Invalid user number.")

  
    elif choice == "4":
        if len(users) == 0:
            print("No users to delete.")
        else:
            for i, user in enumerate(users):
                print(f"{i}. {user}")
            index = int(input("Enter user number to delete: "))
            if 0 <= index < len(users):
                deleted = users.pop(index)
                print(f"{deleted} deleted successfully!")
            else:
                print("Invalid user number.")

   
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select 1-5 only.")