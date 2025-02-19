


import logging
from typing import Optional

logging.basicConfig(
    level=logging.DEBUG,
    filename="safe_divide.txt",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def safe_divide(num1:Optional[int], num2:Optional[int]) ->float: 
    try:
        result = num1 / num2
        logging.info(f"Successful division: {num1} / {num2} = {result}")
        print("Attempted division")
        print("Division was successful")
        return result
    except ZeroDivisionError:
        logging.critical(f"No go, zero division error {ZeroDivisionError}")
        print("Attempted division")
        return "Error: Cannot divide by zero."
    except TypeError:
        logging.critical(f"No go, one or both of the arguments != number {TypeError}")
        print("Attempted division")
        return "Error: Both inputs must be numbers."
        


print(safe_divide(20, 4))  
print(safe_divide(20, 0))  
print(safe_divide(20, "s"))  
print(safe_divide(8, 5))