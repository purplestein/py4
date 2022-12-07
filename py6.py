from itertools import cycle
from itertools import count

for i in count(3):
    if i > 10:
        break
    else:
        print(f'вариант a: {i}')

my_list = [4, 2, 3, 1]
count = 0
for el in cycle(my_list):
    if count > 5:
        break
    print(f'Вариант б: {el}')
    count += 1
