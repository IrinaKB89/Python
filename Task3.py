"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников
имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
f_name = "Test2.txt"
with open(f_name, 'r') as f:
    sal = []
    poor = []
    content = f.read().split()
    for i in content:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
    sal.append(i[1])
print(f'Оклад меньше 20000 {poor}, средний  {sum(map(int, sal)) / len(sal)}')
