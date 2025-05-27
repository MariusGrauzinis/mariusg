import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def year_of_birth(self) -> int:
        return datetime.date.today().year - self.age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __str__(self) -> str:
        return f"Person: {self.name}, Age: {self.age}"


my_person = Person("John", 30)
print(
    f"My personal data: name: {my_person.name}, age: {my_person.age}, dob: {my_person.year_of_birth}"
)


class Student:
    def __init__(self):
        self._score: int = 50

    @property
    def score(self) -> int:
        return self._score + 255

    @score.setter
    def score(self, s: int) -> None:
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError("The score must be between 0 - 100!")

    @score.deleter
    def score(self) -> None:
        self._score = 0
        print("Score deleted!")


Tom = Student()
print(Tom.score)
Tom.score = 75
print(Tom.score)
del Tom.score
print(Tom.score)