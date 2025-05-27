class Animal:
    def speak(self):
        print("Animal can't speak")

class Dog(Animal):
    def speak(self):
        print("Woof woof")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow meow")


Animal().speak()
Dog().speak()
Cat().speak()