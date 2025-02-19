
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="safe_divide.txt",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def devide_numbers(num1:int, num2:int) ->float | None:
    logging.info(f"Dividing number {num1} by number {num2}")
    try:
        return num1 + num2
    except TypeError:
        logging.error(f"No go, one or both of the arguments != number {TypeError}")
        return("Error: Both inputs must be numbers.")
    except ValueError:
        logging.error(f"No go, one or both of the arguments != number {ValueError}")
        return("Both num1 and bnum2 must be of the same type, either both integers or both floats.")

print(devide_numbers(10, "s"))
print(devide_numbers(10, 5))

def get_value_from_dict(data, key):
    try:
        return data[key]
    except KeyError:
        logging.error(f"Error the {key} does not exist in the dictionaty {KeyError}")
        return (f"Error: The key '{key}' does not exist in the dictionary.")


my_dict = {'name': 'Alice', 'age': 30}
print(get_value_from_dict(my_dict, 'gender'))

def 
