# a = int(input('Введите 1 число '))
# b = int(input('Введите 2 число '))
# if a == b*b or b == a*a:
 #   print('да')
#else:
    #print ('нет')

    A = [2, 3, 6, 98, 56, 45, 78, 100, 49]
max = A[0]
for i in A[1:]:
    if i > max:
        max = i
count = 0
for i in A:
    if  max*0.9 < i and i !=max:
        count += 1 
print(count)


