"""Password check program that displays stars based on password length of the users input"""

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    min_length = 5
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

main()
