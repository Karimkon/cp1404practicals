class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}"


def main():
    people = []

    while True:
        first_name = input("Enter first name (or leave blank to finish): ")
        if not first_name:
            break
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        people.append(Person(first_name, last_name, age))

    # Sort by age
    people.sort(key=lambda person: person.age)

    print("\nPeople List:")
    print("First Name | Last Name | Age")
    for person in people:
        print(f"{person.first_name:11} | {person.last_name:9} | {person.age}")


if __name__ == "__main__":
    main()
