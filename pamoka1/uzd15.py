class ImperialToMetric:
    
    @staticmethod
    def inches_to_centimeters(inches: float) -> float:
      
        return round(inches * 2.54, 2)

    @staticmethod
    def feet_to_meters(feet: float) -> float:
       
        return round(feet * 0.3048, 2)

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
      
        return round(miles * 1.60934, 2)

    @staticmethod
    def pounds_to_kilograms(pounds: float) -> float:
      
        return round(pounds * 0.453592, 2)

    @staticmethod
    def gallons_to_liters(gallons: float) -> float:
       
        return round(gallons * 3.78541, 2)



print(ImperialToMetric.inches_to_centimeters(10))
print(ImperialToMetric.feet_to_meters(5))
print(ImperialToMetric.miles_to_kilometers(3))
print(ImperialToMetric.pounds_to_kilograms(150))
print(ImperialToMetric.gallons_to_liters(2))      
