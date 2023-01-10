"""
Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчёте на одного сотрудника.
"""
revenue = int(input("Введите значение прибыль: "))
if revenue <= 0:
    print("Убыток")
else:
    costs = int(input("Введите значение выручка: "))
    profitability = costs/revenue
    print(profitability)
    employees = int(input("Численность сотрудников: "))
    m = revenue / employees
    print(m)
    


