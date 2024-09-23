name = input("Enter name: ")

print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = input(">>> ").upper()

# while loop
while choice != "Q":
    if choice == "H":
        print("Hello " + name)
    elif choice == "G":
        print("Goodbye " + name)
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Get the choice again
    choice = input("---> ").upper()

print(" your menu is finished.")
