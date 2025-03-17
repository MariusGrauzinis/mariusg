
class Vehicles:
    def __init__(self, color):
        self.color = color

    def identify_class(self) -> str:
        return "Vehicle"

    def no_of_wheels(self) -> int:
        return 4

    def print_color(self) -> str:
        return self.color


class Bus(Vehicles):

    def __init__(self, color):
        self.bus_color = color
        super().__init__(color=color)

    def vehicle_class(self) -> str:
        return "Bus"


class Car(Vehicles):

    def __init__(self, color):
        self.car_color = color
        super().__init__(color=color)

    def vehicle_class(self) -> str:
        return "Car"


class Audi(Car):
    def __init__(self, color):
        self.audi_color = color
        super().__init__(color=color)

    def car_brand(self) -> str:
        return "Audi"


my_audi = Audi("red")
print(my_audi.print_color())
print(my_audi.vehicle_class())
print(my_audi.no_of_wheels())
print(my_audi.car_brand())

    

