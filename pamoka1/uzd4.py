


from typing import List


def cout_words(text:List[str]) ->List[str]:
    words_text = [word for word in text.split() if len(word) > 5]
    return - words_text

user_text = input("Enter the text:")
result = cout_words(user_text)
print(result)

