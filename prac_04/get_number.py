def get_number(lower, upper):
    while True:
        try:
            number = float(input(f"Enter a number ({lower}-{upper}): "))
            if lower <= number <= upper:
                return number
            else:
                print(f"Please enter a number between {lower} and {upper}.")
        except ValueError:
            print("Please enter a valid number!")

number = get_number(10, 50)
print("You entered:", number)
