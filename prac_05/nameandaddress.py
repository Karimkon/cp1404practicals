def main():
    addresses = {}

    while True:
        print("\nMenu:")
        print("1. Enter a new name & address")
        print("2. Change an address for an existing entry")
        print("3. Print the address for a name")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter friend's name: ")
            address = input("Enter friend's address: ")
            addresses[name] = address
            print(f"{name}'s address has been added.")

        elif choice == "2":
            name = input("Enter friend's name to update: ")
            if name in addresses:
                address = input("Enter new address: ")
                addresses[name] = address
                print(f"{name}'s address has been updated.")
            else:
                print("Name not found.")

        elif choice == "3":
            name = input("Enter friend's name to look up: ")
            if name in addresses:
                print(f"{name}'s address is: {addresses[name]}")
            else:
                print("Name not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-4.")


if __name__ == "__main__":
    main()
