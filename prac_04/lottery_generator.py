import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_pick():
    """Generates a sorted list of 6 unique random numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)

def main():
    """Main function to run the Quick Pick generator."""
    num_picks = int(input("How many quick picks? "))  # Mistake: No input validation
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

if __name__ == "__main__":
    main()
