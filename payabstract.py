# Task 4: Payment Abstraction

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Cash")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")
