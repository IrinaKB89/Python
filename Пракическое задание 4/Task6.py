"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите
условие его завершения. #### Например, в первом задании выводим целые числа,
начиная с 3. При достижении числа 10 — завершаем цикл. Вторым пунктом
необходимо предусмотреть условие, при котором повторение элементов списка
прекратится.
"""
from itertools import count, cycle
list_int = []
a = int(input("Укажите первое число последовательности >>> "))
n = int(input("Укажите последнее число последовательности "))
for x in count(a):
    if x > n:
        break
    print(x)
    list_int.append(x)