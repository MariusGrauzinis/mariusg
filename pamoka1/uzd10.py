class Animal:
    def __init__(self, color: str, name: str, age: int):
        self.color = color
        self.name = name
        self.age = age

    def identify_class(self) -> str:
        return "Animal"

    def make_sound(self) -> str:
        return "Unknown sound"

    def get_color(self) -> str:
        return self.color

    def get_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}"


class Dog(Animal):
    def __init__(self, color: str, name: str, age: int, breed: str):
        super().__init__(color, name, age)
        self.breed = breed
    def make_sound(self) -> str:
        return "AU AU!"
    def get_color(color) -> str:
        return "Brown"
    def get_name(name) -> str:
        return "Centas"
    def get_age(age) -> int:
        return "3"
    def get_breed(breed) -> str:
        return "Labrador"

    def get_info(self) -> str:
        return f"Dog - Name: {self.name}, Age: {self.age}, Color: {self.color}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, color: str, name: str, age: int, lives_left: int):
        super().__init__(color, name, age)
        self.lives_left = lives_left

    def make_sound(self) -> str:
        return "Meu!"
    def get_age(age) -> int:
        return "9"
    def get_name(name) -> str:
        return "Mafasa"

    def get_info(self) -> str:
        return f"Cat - Name: {self.name}, Age: {self.age}, Color: {self.color}, Lives Left: {self.lives_left}"


class Bird(Animal):
    def __init__(self, color: str, name: str, age: int, can_fly: bool):
        super().__init__(color, name, age)
        self.can_fly = can_fly

    def make_sound(self) -> str:
        return "Cip cip!"
    def get_color(color) -> str:
        return "Yellow"
    def get_name(name) -> str:
        return "Geniukas"
    def fly(can_fly) -> bool:
        return "True"

    def get_info(self) -> str:
        return f"Bird - Name: {self.name}, Age: {self.age}, Color: {self.color}, Can Fly: {self.can_fly}"


My_dog = Dog("Brown", "Centas", 5, "Labrador")
My_cat = Cat("Black", "MUfasa", 3, 9)
My_bird = Bird("Yellow", "Geniukas", 2, True)

print(My_dog.get_info())
print(My_dog.make_sound())

print(My_cat.get_info()) 
print(My_cat.make_sound())

print(My_bird.get_info())
print(My_bird.make_sound())

print(My_dog.get_color())
print(My_bird.fly())