# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
def Fibonacci(n):
    list = []
    firstnum = 1
    secondnum = 1
    for i in range(n):
        list.append(firstnum)
        firstnum,secondnum = secondnum, firstnum + secondnum
    firstnum = 0
    secondnum = 1
    for i in range(n):
        list.insert(0,firstnum)
        firstnum,secondnum = secondnum, firstnum - secondnum
    print(list)
        

n = int(input('Input number '))
Fibonacci(n)