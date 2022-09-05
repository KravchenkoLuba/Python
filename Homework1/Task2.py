# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Введите 1 или 0 '))
y = int(input('Введите 1 или 0 '))
z = int(input('Введите 1 или 0 '))
if (not (x or y or z)) == (not x and not y and not z):
    print(True)
else:
    print(False)    





