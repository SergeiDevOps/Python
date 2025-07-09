from random import randint
import time

#создание класса Игрок

class Player:

    def set_data(self, name, points, iswinner):
        self.name = name
        self.points = points
        self.iswinner = iswinner
     
#Ввод имени с помощью функции в одном модуле
    def get_name(self):
        self.name = input('Введите имя игрока: ')
        return(self.name)
    
#Имитация бросания кубика с помошью функции в одном модуле
    def get_game(self):
        self.points = randint(1, 6)
        return(self.points)

    def get_data(self):
        print(self.name, "points:", self.points)
        
#Определение победителя с помощью функции в одном модуле 
def get_the_winner(w1, w2):
    if w1 > w2:
        return ("Выиграл {0}, очков: {1}".format(p1, w1))
    elif p1 < p2:
        return ("Выиграл {0}, очков: {1}".format(p2, w2))
    else:
        return ("У игроков равное колличество очков")

#Реализация кода игры с использованием класса игрок и функций

print("Введите имена игроков: в данной игре всего два Игрока")

player1 = Player()
player2 = Player()

print("Первый игрок:")
p1 = player1.get_name()
print("Игрок номер 1:", p1)

print("Второй игрок:")
p2 = player2.get_name()
print("Игрок номер 2:", p2)


g1 = player1.get_game()
g2 = player2.get_game()

summ1 = 0
summ2 = 0


for i in range(2):
    for i in range(1):
        print('Кубик бросает', p1)
        time.sleep(2)
        g1 = player1.get_game()
        print('Выпало:', g1)
        summ1 += g1
        sn1 = summ1
        print("Итого очков:", sn1)
        print('Кубик бросает', p2)
        time.sleep(2)
        g2 = player2.get_game()
        print('Выпало:', g2)
        summ2 += g2
        sn2 = summ2
        print("Итого очков:", sn2)
time.sleep(2)    
winner = get_the_winner(sn1, sn2)
print("Победитель:", winner)
