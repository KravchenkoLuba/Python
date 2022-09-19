with open("main.txt","r") as file_obj:
    for line in file_obj:
        if '5' in line:
            line = line.upper()
        list_student.append(line.replace('\n',''))
with open("main.txt", "w") as file_obj:
    for line in list_student:
        file_obj.write(line + '\n')
