


from typing import List


def words_text (text: List[str]) -> List[str]:
  words_with_e =  [word for word in text.split() if "e" in word]
  return words_with_e


user_text = input("Please enter your text: ")

result = words_text(user_text)
print(result)
