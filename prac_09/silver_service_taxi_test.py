from silver_service_taxi import SilverServiceTaxi

def main():
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)  # Fanciness of 2
    fancy_taxi.drive(18)  # Drive 18 km
    print(fancy_taxi)  # Check fare details

if __name__ == '__main__':
    main()
