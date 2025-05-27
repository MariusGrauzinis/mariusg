class Animal:
    def __init__(self, color):
        self.color = color

    def identify_class(self) -> str:
        return "Animal"

    def make_sound(self) -> str:
        return "Unknown sound"

    def get_color(self) -> str:
        return self.color


class Dog(Animal):
    def __init__(self, color):
        self.color = color
        super().__init__(color=color)
        

    def make_sound(self) -> str:
        return "AU AU!"
    def animal_color(self) -> str:
        return "Brown"


class Cat(Animal):
    def __init__(self, color):
        self.color = color
        super().__init__(color=color)


    def make_sound(self) -> str:
        return "Meu"
    def animal_color(self) -> str:
        return "Black"


class Bird(Animal):
    def __init__(self, color):
        self.color = color
        super().__init__(color=color)

    def make_sound(self) -> str:
        return "cip cip!"
    def animal_color(self) -> str:
        return "Yellow"

animal = Dog("Brown")
animal2 = Cat("Black")
animal3 = Bird("Yellow")


print(animal.identify_class())
print(animal.make_sound())
print(animal.get_color())

print(animal2.identify_class())
print(animal2.make_sound())
print(animal2.get_color())

print(animal3.identify_class())
print(animal3.make_sound())
print(animal3.get_color())

