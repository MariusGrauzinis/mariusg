from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def max_speed(self) -> int:
        pass

    def description(self) -> str:
        return f"{self.get_type()} moving {self.max_speed()} km/h ."


class Car(Vehicle):
    def get_type(self) -> str:
        return "Car"

    def max_speed(self) -> int:
        return 180



class Bicycle(Vehicle):
    def get_type(self) -> str:
        return "Bicycle"

    def max_speed(self) -> int:
        return 40



vehicles = [Car(), Bicycle()]

for v in vehicles:
    print(v.description())
