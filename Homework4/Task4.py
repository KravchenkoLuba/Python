#написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.
def encrypt_decrypt(t_string:str, t_key:int, encrypt:bool=True) -> str:
    result = ''
    for i in range(len(t_string)):
        if encrypt:
            result += chr(ord(t_string[i]) + t_key)
        else:
            result += chr(ord(t_string[i]) - t_key)
    return result 

t_string = 'люба'
t_key = int(input('Input key: '))
s_string = encrypt_decrypt(t_string, t_key, True)
with open('Task4.txt','w') as data:
    for i in s_string:
        data.write(i)

with open('Task4.txt','r') as data:
    for i in data:
        f_string = ''
        f_string += i
    print(f_string)  

t_key = int(input('Input key: '))
d_string = encrypt_decrypt(f_string, t_key, False)
print(d_string)

with open('Task4_2.txt','w') as data:
    for i in d_string:
        data.write(i)