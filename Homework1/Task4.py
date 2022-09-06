# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
n = int(input('Input the quarter number: \n' ))
if n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0')
else:
    print('There is no such quarter!')