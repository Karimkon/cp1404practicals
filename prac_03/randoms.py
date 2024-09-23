import random

def main():
    rand_int = random.randint(5, 20)
    print(f"Random integer between 5 and 20: {rand_int}")

    rand_range = random.randrange(3, 10, 2)
    print(f"Random odd number between 3 and 10 (exclusive of 10): {rand_range}")

    rand_uniform = random.uniform(2.5, 5.5)
    print(f"Random float between 2.5 and 5.5: {rand_uniform}")

    rand_num_1_to_100 = random.randint(1,100)
    print(f"Random number between 1 and 100: {rand_num_1_to_100}")

if __name__ == "__main__":
    main()
