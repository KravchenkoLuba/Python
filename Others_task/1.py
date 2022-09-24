# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2

import re

actions = {
  "^": lambda x, y: str(float(x)**float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

def my_eval(expresion: str) -> str:

    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion


exp = "(1 + 5) * (5 * (18 - 2)) / 5"
print(my_eval(exp), eval(exp))

expression = '-22+2'


def get_numbers(expression):
    numbers = []
    temp = ''
    expression += '='
    minus = -1 if expression[0]=='-' else 1
    expression = expression[1:] if expression[0]=='-' else expression
    for char in expression:
        if char.isdigit():
            temp += char
        else:
            numbers.append(temp)
            temp = ''
    numbers = list(filter(lambda char: char.isdigit(), numbers))
    numbers[0] = f'-{numbers[0]}'
    return numbers


def get_operators(expression):
    return list(filter(lambda char: char in '+-*/', expression))


def check_alpha(expression):
    return not any(filter(lambda char: char.isalpha(), expression))


def check_expression(numbers: list, opers: list):
    return True if len(numbers) > len(opers)  else False


if check_alpha(expression):
    numbers = get_numbers(expression)
    list_operators = get_operators(expression)
    if check_expression(numbers, list_operators):
        print(numbers, list_operators)
    else:
        print('Выражение неполное', numbers, list_operators)
else:
    print('Вы ввели буквы')