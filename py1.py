from sys import argv

script_name, name, time, salary, bonus = argv
time = int(time)
salary = int(salary)
bonus = int(bonus)
print(name, time * salary + bonus)
