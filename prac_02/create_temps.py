import random

def main():
    with open("temps_input.txt", "w") as file:
        for _ in range(15):
            temp = random.uniform(-200, 200)
            file.write(f"{temp}\n")

main()
