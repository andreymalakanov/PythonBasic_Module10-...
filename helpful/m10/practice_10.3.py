# Andrey Malakanov
# Skillbox PythonBasic

# Practice 10.3 - 1 

print('Задача 1. Врата')
print()
# Напишите программу, которая выводит в консоль «врата», состоящие из тире, вертикальных линий и пробелов. Поле состоит из 20 строк и 30 столбцов (но не стесняйтесь пробовать и другие размеры).

for row in range(20):
  for col in range(30):
    if row == 0:
      print('-', end = '')
    elif col == 0:
      print('|', end = '')
    elif col == 29:
      print('|', end = '') 
    else:
      print(' ', end = '')
  print()

print('\n' * 5 + '=' * 30, '\n')


# Practice 10.3 - 2 

print('Задача 2. Дорога')
print()
# Мы делаем текстовую игру — гонку, и нам нужно вывести на экран что-то вроде трассы, где будут соревноваться наши машины. Напишите программу, которая выводит такую дорогу на экран (поле 20×50).

for row in range(20):
  for col in range(50):
    if row == 9:
      print('-', end = '')
    elif col == row + 29:
      print('\\', end = '')
    elif col == -row + 19:
      print('/', end = '')
    elif col == 24:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

print('\n' * 5 + '=' * 30, '\n')


# Practice 10.3 - 3 

print('Задача 3. Диагональная матрица ')
print()
# Напишите программу, которая получает на вход размер квадратной матрицы и выводит на экран по такому принципу диагональ из единиц с левого нижнего угла до верхнего правого, ниже диагонали — двойки, выше — нули.

size = int(input('Введите размер матрицы: '))

for row in range(1, size + 1):
  for col in range(1, size + 1):
    if row > col:
      print(2, end = ' ')
    elif row < col:
      print(0, end = ' ')
    else:
      print(1, end = ' ')
  print()

