"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""
f_name = "test.txt"
num_lines = 0
num_words = 0
with open(f_name, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        num_words += len(words)
print(num_words)
# вывод количества слов
print(num_lines)
# вывод количества строк
