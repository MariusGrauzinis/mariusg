
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



    def print_message(message:str) -> str:
  try:
    # doing something with message and so on
    return message
  except Exception as e:
    # printig or logging error