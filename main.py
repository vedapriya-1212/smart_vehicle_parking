# Task 5: Main Program

from parkingspot import ParkingSpot
from parkinglot import ParkingLot
from parking import Vehicle, Bike, Car, Truck, SUV
if __name__ == "__main__":
    # Create Parking Lot & Spots
    lot = ParkingLot("CityMall Parking")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "M"))
    lot.add_spot(ParkingSpot(4, "L"))
    lot.add_spot(ParkingSpot(5, "XL"))

    # Create Vehicles
    bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
    car1 = Car("C201", "TS05CD5678", "Priya", 5)
    suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
    truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

    print("\nVehicles Created:")
    bike1.display()
    car1.display()
    suv1.display()
    truck1.display()

    # Park Vehicles
    lot.park_vehicle(bike1)
    lot.park_vehicle(car1)
    lot.park_vehicle(suv1)
    lot.park_vehicle(truck1)
    lot.show_spots()

    # Unpark + Payment
    lot.unpark_vehicle(car1, hours=3)

    # Final Status
    lot.show_spots()
