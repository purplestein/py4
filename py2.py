gb_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([el for i, el in zip(gb_list, gb_list[1:]) if el > i])

