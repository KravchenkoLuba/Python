# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
list = [1.1, 1.2, 3.1, 5.17, 10.02]

def FractionalPartDifference (list):
    max = 0
    min = 1
    for i in list:
        if  (i - int(i)) > max:
            max = i - int(i)
        elif (i - int(i)) < min:
            min = i - int(i)
    return round((max-min),2)

print(FractionalPartDifference (list))


             

