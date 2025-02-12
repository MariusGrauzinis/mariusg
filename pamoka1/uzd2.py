
from typing import List


def find_numbers (numbers_with_nine: List[int]) ->List[int]:
    numbers_with_nine = [i for i in range(1, 1001) if "9" in str(i)]
    return numbers_with_nine

numbers = list(range(1, 1000))
result = find_numbers(numbers)
print(result)