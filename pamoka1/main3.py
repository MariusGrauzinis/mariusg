# word_list = [ "Tomas", "Jonas", "Petras", "Antanas"]

# def extract_specific_words(word_list: List[str]) -> List[str]:
#     return [name for name in word_list if name.upper().startswith('P')]

# print(extract_specific_words)


# def multiply(num_1: int, num_2: int) -> int:
#     return num_1 * num_2


# print(multiply(2, 2))

# # multiplication = lambda num_1, num_2: num_1 * num_2

# # print(multiplication(2, 5))

# answer = (lambda num_1, num_2: num_1* num_2)(2, 7)
# print(answer)

# a = 5
# b = 7

# answer = (lambda num_1, num_2: num_1 * num_2)(a, b)
# print(answer)

# 3) Use the lambda function to sort list of tuples based on the second element:
# tuples_list = [(1,3), (4,1), (5,2), (2,4)]

# 1) Create a lambda function that takes a number and returns its square.

multiplication = lambda num_1, : num_1 **2
print(multiplication(5))

# 2) Create a lambda function that takes two numbers and returns their squared sum.

multiplication = lambda num_1, num_2 : (num_1 + num_2) **2 
print(multiplication(5, 2))

# 3) Use the lambda function to sort list of tuples based on the second element:

tuples_list = [(1,3), (4,1), (5,2), (2,4)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)

# Use lambda functions to sort list of strings by their length and then alphabetically.

words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'aaa']

sorted_words = sorted(words, key=lambda x: (len(x), x))

print(sorted_words)
