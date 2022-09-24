#  Определить, присутствует ли в заданном списке строк, некоторое число
# ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']

lst = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
a = '6'
res = list(filter(lambda x: a in x, lst))
if len(res) > 0:
    print(f'{a} in the {res} element(s)')
else:
    print('There is no such number in the list')