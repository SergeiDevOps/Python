#Project 1_3B Задание 2.
#Для правильной работы программы установите (импортируйте) модуль "names"
import names
l = []
for i in range(100):
    l.append(names.get_full_name())
print(l)
l1 = []
l2 = []
for name in l:
    if name[0][0] == "A":
       l1.append(name)
    if name[0][0] == "M":
       l1.append(name)
    else:
        l2.append(name)
print(l1)
print(l2)
