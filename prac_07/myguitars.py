import csv

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

    def __str__(self):
        return f"{self.name}, {self.year}, ${self.cost:.2f}"


def read_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_guitar(guitars):
    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = 'guitars.csv'
    guitars = read_guitars(filename)
    guitars.sort()  # Sort guitars by year
    display_guitars(guitars)

    add_guitar(guitars)
    save_guitars(filename, guitars)

    print("\nUpdated guitar list:")
    display_guitars(guitars)


if __name__ == '__main__':
    main()
