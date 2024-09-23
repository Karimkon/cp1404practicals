def read_wimbledon_data(filename):
    """Read Wimbledon data from a CSV file and return it as a list of rows."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            data.append(line.strip().split(","))
    return data


def count_champions(data):
    """Return a dictionary of champions and their win counts."""
    champion_wins = {}
    for row in data[1:]:  # Skip the header row
        champion = row[2]  # Champion's name is in the 3rd column
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
    return champion_wins


def get_unique_countries(data):
    """Return a set of unique countries from the data."""
    countries = set()
    for row in data[1:]:
        if row[1]:  # Avoid empty country values like in 'Cancelled' entries
            countries.add(row[1])  # Country is in the 2nd column
    return countries


def display_champions(champion_wins):
    """Display champions and how many times they have won."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")


def display_countries(countries):
    """Display unique countries in alphabetical order."""
    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def main():
    """Main function to process Wimbledon data and display results."""
    data = read_wimbledon_data("wimbledon.csv")
    champion_wins = count_champions(data)
    countries = get_unique_countries(data)

    display_champions(champion_wins)
    display_countries(countries)


if __name__ == "__main__":
    main()
