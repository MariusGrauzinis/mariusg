import logging
from typing import Optional

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def safe_divide(first_number:Optional[int], second_number:Optional[int])->float:

    try:
        result = first_number/second_number
        print("Attempted division")
        return result
    except ZeroDivisionError:
        logging.critical(f"No go, zero division error {ZeroDivisionError} ")
        print("Division by 0 is not possible")
        return "ERROR"
    except TypeError:
        logging.critical(f"No go, one or both of the arguments != number {TypeError} ")
        print("Both arguments must be numbers")
        return "ERROR"

print(safe_divide(3,4))
print(safe_divide(10, 0))
print(safe_divide(20, "s"))  
print(safe_divide(8, 5))