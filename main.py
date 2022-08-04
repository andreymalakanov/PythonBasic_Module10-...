# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 10. Яма ')

# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

num1 = int(input('Введите число: '))
print()
# print('\n', num1)

for row in range(num1):
  num2 = num1 * 2
  for col in range(num2):
    if col > row and col < num2 - 1 - row:
      print('.', end = '')
    elif col >= num1:
      print(col + 1 - num1, end = '')
    else:
      print(num1 - col, end = '')
  print() 