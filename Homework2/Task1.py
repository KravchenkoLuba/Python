# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n = float(input('input float number: '))
if n < 0:
    n = n*-1
sum = 0
for i in str(n):
 if i != '.':
    sum += int(i)
print(sum)