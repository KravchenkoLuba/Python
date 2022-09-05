#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
n=int(input('Input number from 1 to 7 \n' ))
if n==6 or n==7:
    print('Yes')
elif 6>n>0:
    print('No')
else:
    print('There is no such day of the week!')
