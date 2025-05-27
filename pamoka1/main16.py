
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    salary: float

    def get_name(self) -> str:
        return self.name


# person = Person("John", 30, 1000.0)
# print(person.name)
# print(person.age)
# print(person.salary)
# print(person.get_name())


def get_minimum_salary() -> float:
    return 2000.0


def create_default_person():
    return Person("John", 30, 1000.0)


@dataclass(frozen=True)
class Payment(Person):
    amount: float
    date: str
    description: str = "Payment"
    person: Person = field(default_factory=create_default_person)
    minimum_salary: float = field(default_factory=get_minimum_salary)


payment = Payment(
    name="Anatnas",
    age=10,
    salary=1000.0,
    amount=1000.0,
    date="2023-10-01",
    description="Salary",
)
print(payment)
payment.amount = 2000.0
print(payment.amount)