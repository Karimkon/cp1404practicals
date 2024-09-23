"""Score Menu Program."""

def get_valid_score():
    """Get a valid score with minimum entry"""
    score = 1
    while score < 0 or score > 100:
        score = input("Enter a score (0-100): ")
        score = float(score)
    return score

def print_result(score):
    """Print result based on the score."""
    if score >= 50:
        print("passed!")
    else:
        print("failed.")

def show_stars(score):
    """Show stars based on the score."""
    print("*" * int(score))

def main():
    """Main function for the score menu."""
    print("Welcome to the Score Menu!")
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ")

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()
