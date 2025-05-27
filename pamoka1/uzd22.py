# Create at least 2 class examples that must contain:
#  - class inheritance, encapsulation and polymorphism
#  - several static and classmethods
#  - several methods as property decorators with set and delete functionality.


class Vehicle:
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

    def move(self):
        print(f"{self._brand} vehicle is moving at {self._speed} km/h.")

    @classmethod
    def total_vehicles(cls):
        return cls._vehicle_count

    @staticmethod
    def is_motorized(vehicle_type):
        return vehicle_type.lower() in ['car', 'motorcycle', 'bus']


class Car(Vehicle):
    def move(self):
        print(f"Car {self._brand} is moving at {self._speed} km/h speed.")

class Bicycle(Vehicle):
    def move(self):
        print(f"Bicycle {self._brand} is moving at {self._speed} km/h.")

class Bus(Vehicle):
    def move(self):
        print(f"Bus {self._brand} is moving at {self._speed} km/h.")


v1 = Car("BMW", 150)
v2 = Bicycle("CROSS", 25)
v3 = Bus("Volvo", 90)
v4 = Car("Audi", 120)
v5 = Bicycle("Giant", 30)
v6 = Bus("Mercedes", 80)

v1.move()
v2.move()
v3.move()

print("All Vehicle:", Vehicle.total_vehicles())
