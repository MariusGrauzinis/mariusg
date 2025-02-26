class Car:
    def __init__(self, brand, year, price):
        self.brand = brand  # instance variable/ attribute
        self.year = year
        self.price = price
        self.name = 'Antanas'

    # class instance method
    def get_age(self):
        return 2025 - self.year

    def get_price(self):
        return self.price

    def create_report(self):
        return f"Brand: {self.brand}, Year: {self.year}, Price: {self.price}"
    
    def my_new_method(self):
        pass


my_car = Car(brand="Toyota", year=2015, price=10000)
my_car_2 = Car(brand="Mercedes", year=2018, price=60000)
# print(
#     Car(brand="Toyota", year=2015, price=10000)
#     is Car(brand="Toyota", year=2015, price=10000)
# )
# print(my_car is my_car_2)
# print(my_car.get_age())

# print(my_car.get_price())

print(my_car.create_report())
print(my_car_2.my_new_method())