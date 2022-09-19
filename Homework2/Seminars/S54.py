ef encrypt_decrypt(t_string: str, t_key: int, encrypt: bool = True) -> str:
    '''
    Функция зашифровывает или расшивровывает(определяется последним параметром) принимаемый текст
    '''
    rezult = ''
    for i in range(len(t_string)):
        if encrypt:
            rezult += chr((ord(t_string[i]) + t_key))
        else:
            rezult += chr((ord(t_string[i]) - t_key))

    return rezult
а надо было обязательно только этим же алфавитом шифровать?
