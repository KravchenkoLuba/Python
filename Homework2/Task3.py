# Напишите такую программу, которая найдет палиндром введенного пользователем числа.
def NumberReversal(num):
    rev = 0 
    while(num > 0): 
        dig = num % 10 
        rev = rev * 10 + dig 
        num = num // 10 
    return rev    


def Checkingforapalindrome(num):
    mun =  NumberReversal(num)
    if num == mun: 
        return True
    else:
        return False

def FindPalindrome (num):
    if Checkingforapalindrome(num) is True:
        print("This number is a palindrome!")
    else:
        while Checkingforapalindrome(num) is False:
            num = num + NumberReversal(num)
        print(f"This number - {num} - is a palindrome now!")    

num = int(input('Input number: '))
FindPalindrome (num)
    










# 
# temp = num 
# rev = 0 
# while(num > 0): 
#     dig = num % 10 
#     rev = rev * 10 + dig 
#     num = num // 10 
# if temp == rev: 
#     print("This number is a palindrome!")
# else:
#     print(f"This number is not a palindrome, so num = {temp} + {rev} ={temp+rev} ")  
#     num1 = temp + rev
#     temp1 = num1
#     rev1 = 0
#     while(num1 > 0): 
#         dig1 = num1 % 10 
#         rev1 = rev1 * 10 + dig1 
#         num1 = num1 // 10 
#     if(temp1 == rev1): 
#         print("This number is a palindrome now!") 
