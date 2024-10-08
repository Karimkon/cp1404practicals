from taxi import Taxi

def main():
    # Create a new taxi object
    my_taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40 km
    my_taxi.drive(40)
    print(my_taxi)  # Print taxi's details and the current fare

    # Restart the meter and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)  # Print details and the current fare

if __name__ == '__main__':
    main()
