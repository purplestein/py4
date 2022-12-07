from math import factorial

n = int(input('Ввведите целое число: '))


def fact(n):
    yield n


for el in fact(n):
    print(factorial(n))
