# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def ConvToBinary(num):
    s = ' '
    while num > 0:
        s = str(num % 2) + s
        num = num // 2
    return s 

num = int(input('Input number: '))
print(ConvToBinary(num))




