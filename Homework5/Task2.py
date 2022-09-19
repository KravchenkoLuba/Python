# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

def player_number(name):
    x = int(input(f"{name}, input number from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, input correct number: "))
    return x
name1 = input('What is your name? ')
name2 = input('What is your name? ')
from random import randint
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {name1}")
else:
    print(f"Первый ходит {name2}")
    temp = name1
    name1 = name2
    name2 = temp

number = 20
count1 = 0
count2 = 0
while number > 0:
    player1 = player_number(name1)
    number = number - player1
    count1 += 1
    player2 = player_number(name2)
    number = number - player2
    count2 += 1
if count1 > count2:
    print(f'{name2} won!')
else:
    print(f'{name1} won!')




