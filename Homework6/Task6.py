# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('Input number: '))
lst = [(-3)**i for i in range(0,n)]
print(lst)
