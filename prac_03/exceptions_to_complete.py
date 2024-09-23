result = None

while result is None:
    try:
        user_input = input("Enter an integer: ")
        result = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")

print(f"You entered: {result}")