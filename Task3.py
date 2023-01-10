"""
 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
n = int(input("Введите число n: "))
number = int(n)
double_number = int(number*11)
triple_number = int(number*111)

print(number + double_number + triple_number)
