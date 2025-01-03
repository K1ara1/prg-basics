class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Distance: {self.distance}')
        print(f'Fare: {self.fare}')

def main():
    rider1 = TaxiRide(4)
    rider2 = TaxiRide(5)
    
    rider1.calculate_fare(100)
    rider2.calculate_fare(70)

    print(f'Rider 1: {rider1.print_receipt()}')
    print(f'Rider 2: {rider2.print_receipt()}')

if __name__ == "__main__":
    main()
