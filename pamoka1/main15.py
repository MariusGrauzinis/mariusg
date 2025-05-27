from abc import ABC, abstractmethod
import random


class Person(ABC):
    MY_VALUE = 42

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_age(self, age=5) -> int:
        pass

    def get_birth_year(self) -> int:
        return random.randint(1990, 2000)

    def cacl_smth(self) -> int:
        raise NotImplementedError("This method should be implemented in the subclass")


class Antanas(Person):
    def get_name(self) -> str:
        return "Antanas"

    def get_age(self) -> str:
        return "age"

    def cacl_smth(self) -> int:
        return 42


class Petras(Person):
    pass


my_class = Antanas()
print(my_class.get_age())