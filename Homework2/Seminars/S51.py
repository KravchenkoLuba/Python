a = 'абвгдейка это передача'
list_a = a.split()
print(list_a)
for i in range(len(list_a)):
    if 'абв' in list_a[i]:
        print(i)
        list_a[i] = ''
print(list_a)



2021= S(p1(i) + p1(i)) * i  + p,   i = 1 до  F/k
p(остатотк 2021/27) = 5
к = 28
i = 1 до 72



list1 = ['Python', 'C#', 'C++', 'C++']
list2 = list(range(1, len(list1)+1))
# t = tuple(list1)
# enumerate(list1)
list3 = []
print(list2)
for i in range(len(list1)):
    list3.append(tuple([list2[i], list1[i]]))
print(list3)

for  index_lis in range(len(list3)):
    sum = 0
    elem = list3[index_lis]
    for index_tumpl in range(len(elem[1])):
        sum += ord((elem[1])[index_tumpl])
        # print(ord((elem[1])[index_tumpl]))
    
    if sum%(elem[0]) == 0:
        list3[index_lis] = tuple([sum, list1[index_lis]])
       
    else:
        list3[index_lis] = ''
print(list3)
