try:
    f = open("message.txt", "x")
    f.close()
    print("File created successfully")
except:
    print("File already exist")

while True:
    print("\nWelcome to messaging App")
    print("1. Send message")
    print("2. View Messages")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        msg = input("Type message: ")
        try:
            f = open("message.txt", "a")
            f.write(msg + "\n")
            f.close()
            print("Message sent!")
        except:
            print("Message cannot be sent. Please try again!")

    elif choice == "2":
        try:
            f = open("message.txt", "r")
            print("\nMessages:")
            print(f.read())
            f.close()
        except:
            print("Error reading the file");
    elif choice == "3":
        print("Exiting the program.Goodbye!")
        break

    else:
        print("Invalid input. Please select from option 1-3")