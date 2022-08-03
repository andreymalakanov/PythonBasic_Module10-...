# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|

print()
print('Задача 3. Рамка')
len = int(input('Введите длинну: '))
wid = int(input('Введите ширину: '))

for row in range(len):
  for col in range(wid):
    if row == 0:
      print('_ ', end = '')
    elif col == 0:
      print('| ', end = '')
    elif col == wid - 1:
      print('|', end = '')
    elif row == len - 1:
      print('_ ', end = '')
    else:
      print('  ', end = '')
  print()
