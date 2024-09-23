from car import Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable

    def __init__(self, name, fuel):
        super().__init__(name, fuel)

    def get_fare(self):
        fare = self.price_per_km * self.current_fare_distance
        return round(fare * 10) / 10

    def start_fare(self):
        self.current_fare_distance = 0

    def get_fare(self):
        return self.current_fare_distance * self.price_per_km

    def drive(self, distance):
        self.current_fare_distance += distance
        return super().drive(distance)

    def __str__(self):
        return f"{super().__str__()}, fare: ${self.get_fare():.2f}"
