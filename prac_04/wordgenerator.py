def is_valid_format(format_string):
    valid_chars = {'c', 'v'}
    return all(char in valid_chars for char in format_string)

def get_format():
    while True:
        format_string = input("Enter a sequence of 'c' and 'v': ")
        if is_valid_format(format_string):
            return format_string
        print("Invalid format. Please use only 'c' for consonants and 'v' for vowels.")

format_sequence = get_format()
print("Valid format:", format_sequence)
