class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    @staticmethod
    def calculate_birth_year(age: int) -> int:
        return 2025 - age
    
    @classmethod
    def from_birth_year(cls, birth_year: int) -> int:
        age = 2025 - birth_year
        return age

    @classmethod
    def init_person(cls, age: int) -> "Person":
        age_year = cls.calculate_birth_year(age)
        # doing smth before

        return cls("John", age=age_year) # return Person("John", 30)


my_person = Person("Antanas", 30)
my_second_person = Person.init_person()
print(my_person.get_name())
print(my_second_person.get_name())


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, point_tuple: tuple[float, float]) -> "Point":
        x, y = point_tuple
        return cls(x, y)


point: Point = Point.from_tuple((3, 4))
print(point.x)  # 3
print(point.y)  # 4

import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        age = cls.get_age(birth_year)
        return cls(name, age)

    @staticmethod
    def get_age(birth_year: int) -> int:
        return datetime.date.today().year - birth_year


person: Person = Person.from_birth_year("Petras", 1955)
print(person.name)
print(person.age) 