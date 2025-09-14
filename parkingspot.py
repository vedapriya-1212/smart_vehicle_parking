# Task 2: ParkingSpot Class

class ParkingSpot:
    size_priority = {"S": 1, "M": 2, "L": 3, "XL": 4}
    vehicle_priority = {"Bike": 1, "Car": 2, "SUV": 3, "Truck": 4}

    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size
        self.__occupied = False
        self.__vehicle = None

    def assign_vehicle(self, vehicle):
        vtype = type(vehicle).__name__
        if (not self.__occupied) and (ParkingSpot.vehicle_priority[vtype] <= ParkingSpot.size_priority[self.__size]):
            self.__vehicle = vehicle
            self.__occupied = True
            return True
        return False

    def remove_vehicle(self):
        if self.__occupied:
            v = self.__vehicle
            self.__vehicle = None
            self.__occupied = False
            return v
        return None

    def get_status(self):
        if self.__occupied:
            return f"Occupied → {type(self.__vehicle).__name__} ({self.__vehicle.get_license_plate()})"
        else:
            return "Empty"

    def get_vehicle(self):
        return self.__vehicle

    def get_size(self):
        return self.__size

