"""
Пользователь вводит время в секундах. Переведите время в часы, минуты,
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
time = int(input("Введите время в секундах: "))
hours = int(time/3600)
minutes = int(time/60 - hours*60)
seconds = int(time - minutes*60 - hours*3600)

print(f"Время в формате ч:м:с - {hours}:{minutes}:{seconds}")

