from abc import ABC, abstractmethod

class Vehicle(ABC):
    _vehicle_count = 0

    def __init__(self, brand, speed):
        self._brand = brand
        self._speed = speed
        Vehicle._vehicle_count += 1

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed can't be negative.")
        self._speed = value

    @speed.deleter
    def speed(self):
        print("Transport speed was deleted.")
        self._speed = 0

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def capacity(self):
        pass

    @classmethod
    def total_vehicles(cls):
        return cls._vehicle_count

    @staticmethod
    def is_motorized(vehicle_type):
        return vehicle_type.lower() in ['car', 'motorcycle', 'bus', 'truck',]


class Car(Vehicle):
    def move(self):
        print(f"Car {self._brand} is moving at {self._speed} km/h speed.")

    def fuel_type(self):
        return "Petrol"

    def capacity(self):
        return 5


class Bus(Vehicle):
    def move(self):
        print(f"Bus {self._brand} is moving at {self._speed} km/h speed.")

    def fuel_type(self):
        return "Diesel"

    def capacity(self):
        return 50


class Motorcycle(Vehicle):
    def move(self):
        print(f"Motorcycle {self._brand} is roaring at {self._speed} km/h.")

    def fuel_type(self):
        return "Petrol"

    def capacity(self):
        return 2


class Truck(Vehicle):
    def move(self):
        print(f"Truck {self._brand} is hauling at {self._speed} km/h.")

    def fuel_type(self):
        return "Diesel"

    def capacity(self):
        return 2



v1 = Car("BMW", 150)
v2 = Bus("Volvo", 90)
v3 = Motorcycle("Yamaha", 120)
v4 = Truck("MAN", 80)


v1.move()
v2.move()
v3.move()
v4.move()


print(f"{v1._brand} fuel type: {v1.fuel_type()}")
print(f"{v1._brand} capacity: {v1.capacity()} passengers\n")

print(f"{v2._brand} fuel type: {v2.fuel_type()}")
print(f"{v2._brand} capacity: {v2.capacity()} passengers\n")

print(f"{v3._brand} fuel type: {v3.fuel_type()}")
print(f"{v3._brand} capacity: {v3.capacity()} passengers\n")

print(f"{v4._brand} fuel type: {v4.fuel_type()}")
print(f"{v4._brand} capacity: {v4.capacity()} passengers\n")


print("All Vehicles:", Vehicle.total_vehicles())

