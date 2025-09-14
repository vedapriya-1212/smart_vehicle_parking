# Task 3: ParkingLot Class
from  payabstract import CashPayment, CardPayment, UPIPayment
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
        print(f"Parking Lot Created: {name}")

    def add_spot(self, spot):
        self.spots.append(spot)
        print(f"Spot {spot.spot_id} ({spot.get_size()}) added")

    def show_spots(self):
        print("\nParking Status:")
        for spot in self.spots:
            print(f"Spot {spot.spot_id} ({spot.get_size()}): {spot.get_status()}")

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                print(f"{type(vehicle).__name__} ({vehicle.get_license_plate()}) parked at Spot {spot.spot_id}")
                return True
        print(f"No suitable spot available for {type(vehicle).__name__}")
        return False

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"{type(vehicle).__name__} ({vehicle.get_license_plate()}) removed from Spot {spot.spot_id}")
                print(f"Parking Fee = ₹{fee}")
                self.process_payment(fee)
                return
        print("Vehicle not found in lot!")

    def process_payment(self, amount):
        print("Select Payment Method: 1. Cash 2. Card 3. UPI")
        choice = int(input("Enter choice: "))
        if choice == 1:
            CashPayment().process_payment(amount)
        elif choice == 2:
            CardPayment().process_payment(amount)
        elif choice == 3:
            UPIPayment().process_payment(amount)
        else:
            print("Invalid choice!")

