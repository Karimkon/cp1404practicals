from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    while True:
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        option = input(">>> ").lower()

        if option == 'q':
            break
        elif option == 'c':
            for i, taxi in enumerate(taxis):
                print(f"{i}: {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif option == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("How far do you want to drive? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                total_bill += fare
                print(f"Trip cost: ${fare:.2f}, Total bill: ${total_bill:.2f}")
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
