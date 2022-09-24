#  Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
list_num = [11, 2, 7, 4, 5, 6]
res = [(list_num[i] * list_num[-i-1]) for i in range(math.ceil(len(list_num)/2))]
print(res)




