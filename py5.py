from functools import reduce


def reduce_func(el_prev, el):
    return el - el_prev


my_list = [el for el in range(99, 1001) if not el % 2]
print(reduce(reduce_func, my_list))
