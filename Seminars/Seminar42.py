# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве 
# символа-разделителя используйте пробел.



a = str(input("Введите числа через пробел: "))
list_of_str = a.split(" ")
print(list_of_str)
list_of_num = []
for i in list_of_str:
    list_of_num.append(int(i))
min = list_of_num[0]
max = min
for i in list_of_num:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)
