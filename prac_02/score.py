"""Score evaluation program."""

import random

def evaluate_score(score):
    """checking the score and return the results that are got."""
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(f"Your score is {score}. Result: {result} thank you so much")

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}. Result: {evaluate_score(random_score)}")

main()
