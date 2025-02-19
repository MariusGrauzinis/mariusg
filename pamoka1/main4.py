
# try:
#     print("I am here!")
#     print(2 / 0)
# except Exception as e:
#     print(f"Learn some basic math dude!,because off error: {e}")


# try:
#     # print("I am here!")
#     print(2 / 0)
# except ZeroDivisionError:
#     print(f"CAN'T DIVIDE BY ZERO!")


# try:
#     input = int(input("Enter a number: "))
#     print(input)
# except Exception as e:
#     print(f"Error: {e}")



#   def print_message(message:str) -> str:
# try:
#   # doing something with message and so on
#   return message
# except Exception as e:
# printig or logging error
# try:
#     input = 25 / 0
#     print(input)
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print("No error occured")
# finally:
#     print("I will always run")

# try:
#     input = 25 / 0
#     print(input)
# except Exception as e:
#     print(f"Error: {e}")

def divide_numbers(x: int, y: int) -> float:
    logging.info(f"Dividing number {x} by number {y}")
    try:
        return x / y
    except ZeroDivisionError as e:
        logging.exception(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
    except TypeError as e:
        logging.exception(f"Wrote a letter or word, {e}")
        print(f"Your input is not a number, {e}")
print(divide_numbers(10, "a"))