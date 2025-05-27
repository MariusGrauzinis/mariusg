class Pet:
    def __init__(self, name: str, age: int = 0) -> None:
        self.name = name
        self.age = age

    def set_name(self, name: str) -> None:
        self.name = name

    def set_age(self, age: int) -> None:
        self.age = age


my_pet = Pet("Dog")
print(my_pet.name)
my_pet.set_name("Cat")
my_pet.set_age(5)
print(my_pet.name)
print(my_pet.age)


class Pet:
    def __init__(self) -> None:
        self.name = None
        self.age = None
        self.color = None

    def set_name(self, name: str) -> "Pet":
        self.name = name
        return self

    def set_age(self, age: int) -> "Pet":
        self.age = 2025 - age
        # self.age = age
        return self

    def set_color(self, color: str) -> "Pet":
        # doing smth before
        self.color = color
        return self


my_pet = Pet()
my_pet.set_name("Cat").set_age(5).set_color("Black")
print(my_pet.name)
print(my_pet.age)
print(my_pet.color)