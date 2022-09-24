# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from math import sqrt
x = input('Input the coordinates of the first point, separated by a space: ')
x = list(map(int, x.split(' ')))
y = input('Input the coordinates of the second point, separated by a space: ')
y = list(map(int, y.split(' ')))

distance = round(sqrt((x[0] -y[0])**2 + (x[1]-y[1])**2), 2)
print(f'Distance is {distance}')