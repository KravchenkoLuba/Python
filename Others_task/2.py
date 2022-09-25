str = '2+5-(3+10)'
def calk(str):
    lst_num = []
    lst_oper = []
    first_lst = str.split(' ')
    print(first_lst)
    for elem in first_lst:
        # if elem == '(':
        #     while elem == ')':
        #         calk()
        if elem.isdigit():
            lst_num.append(elem)
        elif elem.isalpha():
            lst_oper.append(elem)
    return lst_num, lst_oper

res = calk(str)
print(res)
