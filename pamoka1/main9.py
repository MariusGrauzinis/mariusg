



# int_one = 10
# int_two = 15
# print(int_one + int_two)

# str_one = "10"
# str_two = "15"

# print(str_one + str_two)

# str_one = "animal"

# print(len(str_one))

class Phones:
    def __init__(self, model):
        self.model = model

    def phone_brand(self) -> str:
        return "Antanaphonas"

    def phone_model(self) -> str:
        return self.model


class Samsung(Phones):
    def __init__(self, model):
        super().__init__(model=model)
        print(super().phone_brand())

    def phone_brand(self) -> str:
        print(super().phone_brand())
        return "Samsung"
    
my_samsung = Samsung(model="Galaxy")

print(my_samsung.phone_brand())
print(my_samsung.phone_model())