from unreliable_car import UnreliableCar

def main():
    my_unreliable_car = UnreliableCar("Old Car", 100, 50)
    distance_driven = my_unreliable_car.drive(40)
    print(f"Distance driven: {distance_driven} km")

if __name__ == '__main__':
    main()
