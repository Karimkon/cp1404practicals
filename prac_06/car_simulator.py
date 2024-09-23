class Car:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.odo = 0

    def drive(self, km):
        if km < 0:
            print("Distance must be >= 0")
            return
        if km > self.fuel:
            km = self.fuel
            print(f"The car drove {km}km and ran out of fuel.")
        else:
            print(f"The car drove {km}km.")
        self.odo += km
        self.fuel -= km

    def refuel(self, amount):
        if amount < 0:
            print("Fuel amount must be >= 0")
            return
        self.fuel += amount
        print(f"Added {amount} units of fuel.")

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odo}"

def main():
    car_name = input("Enter your car name: ")
    car = Car(car_name)

    while True:
        print(car)
        print("Menu:")
        print("d) drive")
        print("r) refuel")
        print("q) quit")
        choice = input("Enter your choice: ").lower()

        if choice == 'd':
            km = int(input("How many km do you wish to drive? "))
            car.drive(km)
        elif choice == 'r':
            amount = int(input("How many units of fuel do you want to add to the car? "))
            car.refuel(amount)
        elif choice == 'q':
            print(f"Good bye {car.name}'s driver.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
