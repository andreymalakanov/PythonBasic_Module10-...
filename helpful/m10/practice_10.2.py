# Andrey Malakanov
# Skillbox PythonBasic

# Practice 10.2 - 1 

# Напишите программу, которая выводит квадратную матрицу размера N на N. В каждой нечётной строке матрицы идут числа от 1 до N, а в каждой чётной — просто числа, равные номеру этой строки.

print('Задача 1. Матрица')

size = int(input('Введите размер матрицы: '))

for row in range(1, size + 1):
  for col in range(1, size + 1):
    if row % 2 != 0:
      print(row, end = ' ')
    else:
      print(col, end = ' ')
  print()

print('\n' + '=' * 20, '\n')


# Practice 10.2 - 2

print('Задача 2. Чёрный ящик')

size = int(input('Введите размер матрицы: '))

for row in range(1, size + 1):
  for col in range(1, size + 1):
    if col % 3 != 0:
      print(row, end = ' ')
    else:
      print(col, end = ' ')
  print()

print('\n' + '=' * 20, '\n')

# Practice 10.2 - 3

print('Задача 3. Координатные оси')

# Напишите программу, которая рисует координатные оси на поле 20×50.

for row in range(20):
  for col in range(50):
    if row == 9:
      print('-', end = '')
    elif col == 24:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()