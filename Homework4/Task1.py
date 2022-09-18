# Задайте натуральное число N. Напишите программу, которая составит список простых множителей
# числа N
def FindPrimeFactors(N):
    list = []
    i = 2
    while i <= N:
        if N % i == 0:
            list.append(i)
            N = N // i
            i = 2
        else:
            i += 1
    return list
N = int(input('Input number: '))
print(f'{N} -> {FindPrimeFactors(N)}')