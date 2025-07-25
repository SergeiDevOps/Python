#Функции для возведения числа в степень
#
#Возведение в степень с использованием модуля math
import math
def degree(a, b):
    s = pow(a, b)
    return s
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", degree(a, b))

#Возведение в степень с использованием рекурсии
def degree1(c, d):
    if (d == 1):
        return (c)
    if (d != 1):
        return (c * degree1(c, d - 1))
c = int(input("Введите число: "))
d = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", degree1(c, d))

#Возведение в степень с использованием оператора "**"
def degree2(e, f):
    s1 = e ** f
    return s1
e = int(input("Введите число: "))
f = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", degree2(e, f))

    
