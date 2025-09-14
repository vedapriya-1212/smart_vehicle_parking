# Task 1: Vehicle Classes
from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self, vehicle_id, license_plate, owner_name):
        self.vehicle_id = vehicle_id
        self.__license_plate = license_plate  
        self.__owner_name = owner_name        

    # Encapsulation: Getters & Setters
    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, plate):
        self.__license_plate = plate

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, name):
        self.__owner_name = name

    def display(self):
        print(f"Vehicle → ID: {self.vehicle_id}, Plate: {self.__license_plate}, Owner: {self.__owner_name}")

    def calculate_parking_fee(self, hours):
        raise NotImplementedError("Subclass must implement this method")


class Bike(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, helmet_required):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, seats):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, four_wheel_drive):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, max_load_capacity):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 100 * hours