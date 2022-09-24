# дорешать задачу с семинара

def check_isalpha(str):
    for i in str:
        if i.isalpha():
            return True

def creat_lst_num(expression):
    lst_num = []
    expression = expression + ' '
    temp = ''
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            lst_num.append(temp)
            temp = ''
    lst_num = list(filter(lambda x: x != '', lst_num))
    lst_num = list(map(float, lst_num))
    return lst_num

def creat_lst_oper(expression):
    lst_oper = list(filter(lambda x: x == '+' or x == '-' or x == '*' or x == '/', expression))
    return lst_oper

def reduce_lst(i, list1, list2):
    del list1[i+1]
    del list2[i]
    return list1, list2

def calcul(lst_num, lst_oper):
    while len(lst_oper) > 0:
        while '/' in lst_oper:
            for i, element in enumerate(lst_oper):
                if element == '/':
                    lst_num[i] = lst_num[i] / lst_num[i+1]
                    reduce_lst(i, lst_num, lst_oper)
        while '*' in lst_oper:
            for i, element in enumerate(lst_oper):
                if element == '*':
                    lst_num[i] = lst_num[i] * lst_num[i+1]
                    reduce_lst(i, lst_num, lst_oper)
        while '-' in lst_oper:
            for i, element in enumerate(lst_oper):
                if element == '-':
                    lst_num[i] = lst_num[i] - lst_num[i+1]
                    reduce_lst(i, lst_num, lst_oper)
        while '+' in lst_oper:
            for i, element in enumerate(lst_oper):
                if element == '+':
                    lst_num[i] = lst_num[i] + lst_num[i+1]
                    reduce_lst(i, lst_num, lst_oper)
    return lst_num[0]

while True:
    try:
        your_example = input('Input your example:  ')
        if check_isalpha(your_example):
            print('These are not numbers!')
        else:
            lst_num = creat_lst_num( your_example)
            print(f'Список чисел {lst_num}')
            lst_oper = creat_lst_oper(your_example)
            print(f'Список операций {lst_oper}')
            print(f'{your_example} = {calcul(lst_num, lst_oper)}')
            break
    except:
        print('Not enough numerical data')