# Andrey Malakanov
# Skillbox PythonBasic

# Practice 10.1 - 1 

# Таблица умножения от 1 до 9. Только ответ.

print('Задача 1. Таблица умножения')

for a in range(1,10):
  for b in range(1, 10):
    answer = a * b
    print(answer, end = '\t')
  print('\n')

print('\n' + '=' * 20, '\n')

# Practice 10.1 - 2

# Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N.

print('Задача 2. Таблица суммы')

N = int(input('Введите число: '))
for row in range(N + 1):
  for col in range(N + 1):
    answer = row + col
    print(answer, end = '\t')
  print()

print('\n' + '=' * 20, '\n')
  
# Practice 10.1 - 3

# Почить туже таблицу:
# 0   -1  -2  -3  -4  -5  -6  -7  -8  -9
# 1   0   -1  -2  -3  -4  -5  -6  -7  -8
# 2   1   0   -1  -2  -3  -4  -5  -6  -7
# 3   2   1   0   -1  -2  -3  -4  -5  -6
# 4   3   2   1   0   -1  -2  -3  -4  -5
# 5   4   3   2   1   0   -1  -2  -3  -4
# 6   5   4   3   2   1   0   -1  -2  -3
# 7   6   5   4   3   2   1   0   -1  -2
# 8   7   6   5   4   3   2   1   0   -1
# 9   8   7   6   5   4   3   2   1   0

print('Задача 3. Анализ данных')

for row in range(10):
  for col in range(10):
    answer = row - col
    print(answer, end = '\t')
  print()

print('\n' + '=' * 20, '\n')



