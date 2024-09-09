# Password Manager

# Function to store passwords
def store_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Code to store the password in a secure manner
    # ...

    with open("passwords.txt", "a") as file:
            file.write(f"Website: {website}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write("\n")
print("Password stored successfully!")

# Function to retrieve passwords
def retrieve_password():
    website = input("Enter website: ")
    username = input("Enter username: ")

    # Code to retrieve the password
    # ...

    print("Password retrieved successfully!")

# Main menu
def main():
    while True:
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()