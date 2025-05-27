class Car:
    total_cars_sold: int = 0

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        Car.total_cars_sold += 1

    @classmethod
    def get_total_cars_sold(cls) -> int:
        return cls.total_cars_sold


my_car = Car("Toyota", "Corolla")
print(Car.get_total_cars_sold())
my_second_car = Car("Honda", "Civic")
print(Car.get_total_cars_sold())
my_third_car = Car("Ford", "Mustang")
my_fourth_car = Car("Chevrolet", "Camaro")
print(Car.get_total_cars_sold())


class Student:
    all_students: list["Student"] = []

    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade
        Student.all_students.append(self)
        print(self.all_students)

    def __repr__(self) -> str:
        return f"Student(name={self.name}, grade={self.grade})"

    def __str__(self) -> str:
        return f"Student: {self.name}, Grade: {self.grade}"

    @classmethod
    def get_highest_grade(cls) -> "Student":
        return max(cls.all_students, key=lambda student: student.grade)

    @classmethod
    def get_lowest_grade(cls) -> "Student":
        return min(cls.all_students, key=lambda student: student.grade)


student1: Student = Student("John", 90)
student2: Student = Student("Jane", 95)
student3: Student = Student("Alice", 80)
student4: Student = Student("Bob", 85)

greates_student = Student.get_highest_grade()
print(greates_student.name, greates_student.grade)