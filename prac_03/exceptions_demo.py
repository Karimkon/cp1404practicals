"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters a non-integer value for the numerator or denominator.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user enters zero as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
No, it's not possible to avoid a ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
