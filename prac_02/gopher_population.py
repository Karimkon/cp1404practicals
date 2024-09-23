import random
def simulate_gophers_method():
    population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {population}")

    for year in range(1, 11):
        births = random.randint(int(population * 0.1), int(population * 0.2))
        deaths = random.randint(int(population * 0.05), int(population * 0.25))
        population += births - deaths

        print(f"\nYear {year}")
        print(f"{births} gophers were born and {deaths} died.")
        print(f"Population: {population}")


simulate_gophers_method()
