# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 


list0 = ['Python', 'C#', 'C++', 'C++']
list1 = list(map(lambda i: i.upper(),list0))
list2 = list(range(1, len(list1)+1))
def Create_list_from_two(list1,list2):
    list3 = list(zip(list1,list2))
    return list3
list3 = Create_list_from_two(list2,list1)
print(list3)

def Sum_of_points_divisor(list_cor):
    for  index_lis in range(len(list_cor)):
        sum = 0
        elem = list_cor[index_lis]
        for index_tumpl in range(len(elem[1])):
            sum += ord((elem[1])[index_tumpl])
        if sum%(elem[0]) == 0:
            list_cor[index_lis] = tuple([sum, list1[index_lis]])
       
        else:
            list_cor.remove(list_cor[index_lis]) 
    return list_cor 

rez_list = Sum_of_points_divisor(list3)
print(rez_list)


