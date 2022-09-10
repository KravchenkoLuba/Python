# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [2,3,4,5,6]

def ProductOfPairsOfNumbers(list):
    i1 = 0
    i2 = -1
    list2 = []
    while i1 < len(list)/2:
        temp = list[i1] * list[i2]
        list2.append(temp)
        i1 += 1
        i2 -=1
    return list2    
print(ProductOfPairsOfNumbers(list))