def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            data.append(line.strip().split(","))
    return data


def count_champions(data):
    champion_wins = {}
    for row in data[1:]:
        champion = row[2]  # Champion's name
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
    return champion_wins


def count_losses(data):
    """Return a dictionary of players with the most losses in finals."""
    finalist_losses = {}
    for row in data[1:]:
        finalist = row[3]  # Finalist's name
        if finalist in finalist_losses:
            finalist_losses[finalist] += 1
        else:
            finalist_losses[finalist] = 1
    return finalist_losses


def country_finalists(data):
    country_counts = {}
    for row in data[1:]:
        country = row[1]  # Country of the finalist
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    return country_counts


def main():
    data = read_wimbledon_data("wimbledon.csv")

    while True:
        print("\nMenu:")
        print("1. Champions sorted by most wins")
        print("2. Players who lost the most finals")
        print("3. Countries by number of finalists")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            champions = count_champions(data)
            for champion, wins in sorted(champions.items(), key=lambda item: item[1], reverse=True):
                print(f"{champion}: {wins} wins")

        elif choice == "2":
            losers = count_losses(data)
            for player, losses in sorted(losers.items(), key=lambda item: item[1], reverse=True):
                print(f"{player}: {losses} losses")

        elif choice == "3":
            countries = country_finalists(data)
            for country, count in sorted(countries.items(), key=lambda item: item[1], reverse=True):
                print(f"{country}: {count} finalists")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-4.")


if __name__ == "__main__":
    main()
