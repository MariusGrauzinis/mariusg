def puzzle_pieces(list1, list2):
    if len(list1) != len(list2):
        return False
    
    sum_value = list1[0] + list2[0]
    
    for i in range(1, len(list1)):
        if list1[i] + list2[i] != sum_value:
            return False
    
    return True

print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))
print(puzzle_pieces([1, 2], [-1, -1]))
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))