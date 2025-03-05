class Student:
    def __init__(self, name: str, age: int, mark: int):
        self.name = name
        self.age = age
        self.mark = mark
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Mark: {self.mark}"

    def student_name(self) -> str:
        return f"Name:{self.name}"
    
    def student_mark(self)->int:
        return f"Mark:{self.mark}"
    
    def student_age(self)-> int:
        return f"Age:{self.age}"
    



Student1 = Student("Jonas" , 21, [9, 9, 8, 7])
Student2 = Student("Petras", 19, [10, 10, 9, 10])
Student3 = Student("Martynas", 20, [8, 7, 6, 10])
Student4 = Student("Bonifacijus", 22, [9, 8, 6, 10])

print(Student2.student_name())
print(Student3.student_mark())
print(Student4.student_age())
print(Student4.student_name())
print(Student4.get_info())