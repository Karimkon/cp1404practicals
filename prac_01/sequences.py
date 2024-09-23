print("Welcome to the number sequence generator!")
x = int(input("Enter the start number x: "))
y = int(input("Enter the end number y: "))

choice = ""

if choice != "4":
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares of the numbers from x to y")
    print("4. Exit the program")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Even numbers between", x, "and", y)
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end="")
        print("\n")

    elif choice == "2":
        print("odd numbers between x and y")
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end="")
        print("\n")

    elif choice == "3":
        print("Squares of numbers between", x, "and", y)
        for i in range(x, y + 1):
            print(i ** 2, end="")
        print()

    elif choice == "4":
        print("Exiting the program.")

    else:
        print("Invalid choice.")

print("Program ended.")
