"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []
try:
    with open('file_4.txt', 'r') as file_obj:
        for line in file_obj:
            i = line.split(' ', 1)
            new_text.append(num[i[0]] + '  ' + i[1])
            print(new_text)
    with open('file_4_new.txt', 'w') as file_obj_2:
        file_obj_2.writelines(new_text)
except IOError:
    print("Произошла ошибка ввода-вывода!")
