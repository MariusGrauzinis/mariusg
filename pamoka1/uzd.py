# You have a list of ten random words which starts with letters A, C, or P.
# Write a function that takes a list of the word_list and prints new list 
# with all words that starts with letter P.


# from typing import List


# word_list = ["Ananasas", "Paprika", "Cunamis", "Citrina", "Automobilis", "Pienas", "Akis", "Ausis", "Puma", "Aklas"]


# def filter_words(word_list:List[str]) ->List[str]:
#     p_words: List[str] = []
#     for word in word_list:
#         if word.startswith('P'):
#             p_words.append(word)
#     return p_words

# print(filter_words(word_list)) 



# from typing import List


# word_list = [ "Tomas", "Jonas", "Petras"]

# def extract_specific_words(word_list: List[str]) -> List[str]:
#     return [name for name in word_list if name.upper().startswith('P')]

# print(extract_specific_words)

from typing import List


def devides_number (numbers2: List[int]) -> List[int]:
    numbers2 = [numbers for numbers in range(1, 1000) if numbers % 6 == 0]
    return numbers2

numbers = list(range(1, 1000))
result = devides_number(numbers)
print(result)
