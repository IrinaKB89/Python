"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать
пустая строка.
"""
mf_n = open("text.txt", 'w')
entry = input("Введите данные: ")
while entry:
    mf_n.writelines(entry + '\n')
    entry = input()
    if entry == '':
        break
mf_n.close()

mf_n = open('test.txt', 'r')
content = mf_n.readlines()
print(content)
mf_n.close()
