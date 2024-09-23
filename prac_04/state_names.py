"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Dictionary of Australian state codes and names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the state code dictionary
print(CODE_TO_NAME)

# Prompt user for state code
state_code = input("Enter short state: ").upper()  # Convert input to uppercase
while state_code != "":
    try:
        # Try to print the full state name
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        # Handle invalid state codes
        print("Invalid short state")

    state_code = input("Enter short state: ").upper()  # Convert input to uppercase

# Print all states and names
print("\nAll states and their names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")  # Align output neatly
