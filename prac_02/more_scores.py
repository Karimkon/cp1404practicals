import random

def get_result(score):
    if score >= 85:
        return f"{score} is Excellent"
    elif score >= 50:
        return f"{score} is Passable"
    else:
        return f"{score} is Bad"

def main():
    num_scores = int(input("Enter the number of scores: "))
    with open("results.txt", "w") as file:
        for _ in range(num_scores):
            score = random.randint(0, 100)
            result = get_result(score)
            file.write(result + "\n")

main()
