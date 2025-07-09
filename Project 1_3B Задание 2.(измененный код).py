#Project 1_3B Задание 2.
#Для правильной работы программы установите (импортируйте) модуль "names"
import names

l = []
for i in range(100):
    l.append(names.get_first_name())
l = sorted(l)
print(l)

l1 = []
l2 = []

for name in l:
    if name[0]>="A" and name[0]<="M":
        l1.append(name)
    else:
        l2.append(name)
l1 = sorted(l1)
l2 = sorted(l2)
print(l1)
print(l2)
