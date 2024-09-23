"""
Email Storage Program
Estimate: 20 minutes
Actual:   30 minutes
"""


def extract_name(email):
    """Extracts a name from the email by splitting the string."""
    name_part = email.split('@')[0]  # Get the part before the '@'
    name_parts = name_part.split('.')  # Split by dots
    name = ' '.join(name_parts).title()  # Join and capitalize
    return name


# Dictionary to store email and names
email_dict = {}

# Prompt the user for their email
while True:
    email = input("Email: ")
    if email == "":
        break  # Exit loop if blank email is entered

    # Extract name from email
    name = extract_name(email)

    # Ask for confirmation
    confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if confirm != '' and confirm != 'y':
        name = input("Name: ")

    # Store the email and name in the dictionary
    email_dict[email] = name

# Print the stored emails and names
for email, name in email_dict.items():
    print(f"{name} ({email})")
