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

    










