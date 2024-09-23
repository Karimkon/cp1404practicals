import json

def load_addresses(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_addresses(filename, addresses):
    with open(filename, "w") as file:
        json.dump(addresses, file)

def main():
    filename = "addreses.json"
    addresses = load_addresses(filename)

    while True:
        print("\nMenu:")
        print("1. Enter a new name & addres")
        print("2. Change an addres for an existing entry")
        print("3. Print the addres for a name")
        print("4. Save and Quit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter friend's name: ")
            address = input("Enter friend's addres: ")
            addresses[name] = address
            print(f"{name}'s addres has been added.")

        elif choice == "2":
            name = input("Enter friend's name to update: ")
            if name in addresses:
                address = input("Enter new addres: ")
                addresses[name] = address
                print(f"{name}'s addres has been updated.")
            else:
                print("Name not found.")

        elif choice == "3":
            name = input("Enter friend's name to look up: ")
            if name in addresses:
                print(f"{name}'s addres is: {addresses[name]}")
            else:
                print("Name not found.")

        elif choice == "4":
            save_addresses(filename, addresses)
            print("Addreses saved. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-4.")


if __name__ == "__main__":
    main()
