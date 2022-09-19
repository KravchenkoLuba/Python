# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

with open('file1.txt','w') as file_obj:
    first_s = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
    for i in first_s:
        file_obj.write(i)
with open('file1.txt','r') as file_obj:    
    s = ''
    for i in file_obj:
        s += i   

def encode(s):
    s_encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count +1
            i = i + 1
        s_encoding += str(count) + s[i]
        i = i + 1
    return s_encoding
print(encode(s))
second_s = encode(s)
with open('file2.txt','w') as data:
    for i in second_s:
        data.write(i)

with open('file2.txt','r') as data:
    third_s = ''
    for i in data:
        third_s += i
    print(third_s)

def decode(s):
    s_decoding = ''
    count1 = ''
    i = 0
    for i in third_s:
        if i.isdigit():
            count1 += i
        else:
            s_decoding += int(count1)*i
            count1 = ''
    return s_decoding

print(decode(third_s))

