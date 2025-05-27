class Temperature:
    def __init__(self, kelvin):
        if kelvin < 0:
            raise ValueError("Kelvin temperature cannot be less than 0!")
        self.kelvin = kelvin

    def __str__(self):
        celsius = self.kelvin_to_celsius(self.kelvin)
        fahrenheit = self.kelvin_to_fahrenheit(self.kelvin)
        return f"Temperature: {self.kelvin}K, {celsius:.1f}°C, {fahrenheit:.1f}°F"

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32



temp = Temperature(300)
print(temp)

print(Temperature.kelvin_to_celsius(300))
print(Temperature.kelvin_to_fahrenheit(300))