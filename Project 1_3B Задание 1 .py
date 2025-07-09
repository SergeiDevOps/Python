#Project 1_3B Задание 1.
from random import randint
l = [randint(1,100) for i in range(100)]
l = sorted(l)
print(l, type(l))
s = int(input("Введите пороговое значение: "))
l1 = []
for i in l:
    if i < s:
        l1.append(i)
        l1.append("Низкий")
    if i > s:
        l1.append(i)
        l1.append("Высокий")
print(l1)


