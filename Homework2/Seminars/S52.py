import random
n = random.randint(1,10)
print(f"Натуральная степень {n}")
list1 = [random.randint(1,100)]
for i in range(1, n + 1):
    list1.append(random.randint(0,100))
print(f"Список коэффициентов: {list1}")
list_x = []
for i in range(n + 1):
    list_x.insert(0, "x**" + str(i))
print(list_x)

polinom = list(zip(list1, list_x))
print(polinom)
