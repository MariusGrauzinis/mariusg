from typing import List


def puzzle_pieces(First_list:List[int], Second_list:list[int]) ->  bool:
    if len(First_list) != len(Second_list):
        return False

    sums = []
    for i in range(len(First_list)):
        sums.append(First_list[i] + Second_list[i])

    if len(set(sums)) == 1:
        return True
    else:
        return False

print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))
print(puzzle_pieces([1, 2], [-1, -1]))
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))