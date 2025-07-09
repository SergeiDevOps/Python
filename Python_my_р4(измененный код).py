from random import randint
import time
gamer1 = input('Введите имя 1-го играющего ')
gamer2 = input('Введите имя 2-го играющего ')
summ1 = 0
summ2 = 0
for i in range(2):
    for i in range(1):
        print('Кубик бросает', gamer1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        summ1 += n1
        sn1 = summ1
        print("Итого очков:", sn1)
    for i in range(1):
        print('Кубик бросает', gamer2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        summ2 += n2
        sn2 = summ2
        print("Итого очков:", sn2)
time.sleep(2)    
if sn1 > sn2:
 print('Выиграл', gamer1)
elif sn1 < sn2:
 print('Выиграл', gamer2)
else:
 print('Ничья')
