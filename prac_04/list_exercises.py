# Basic list operations function
def basic_list_operations():
    numbers = []

    for _ in range(5):
        num = float(input("Enter a number: "))
        numbers.append(num)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.2f}")


# Woefully inadequate security checker
def security_checker():
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole',
        'InterpreterInterface', 'StartServer', 'bob'
    ]

    username = input("Enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Main function to run both exercises
def main():
    print("Basic List Operations:")
    basic_list_operations()
    print("\nWoefully Inadequate Security Checker:")
    security_checker()


if __name__ == "__main__":
    main()
