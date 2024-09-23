# variabels
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def is_valid_password(password):
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        print("Your password must be between {} and {} characters.".format(MIN_LENGTH, MAX_LENGTH))
        return False

    has_lower = has_upper = has_digit = has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif SPECIAL_CHARACTERS_REQUIRED and char in SPECIAL_CHARACTERS:
            has_special = True

    if not has_lower:
        print("Your password must contain at least 1 lowercase character.")
    if not has_upper:
        print("Your password must contain at least 1 uppercase character.")
    if SPECIAL_CHARACTERS_REQUIRED and not has_special:
        print("Your password must contain at least 1 special character: {}".format(SPECIAL_CHARACTERS))

    return has_lower and has_upper and has_digit and (not SPECIAL_CHARACTERS_REQUIRED or has_special)


def main():
    while True:
        password = input("Please enter a correct password ")
        if is_valid_password(password):
            print(f"Your {len(password)} character password is valid: {password}!")
            break
        else:
            print("Invalid password!")


if __name__ == "__main__":
    main()
