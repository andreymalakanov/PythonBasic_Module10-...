# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)

# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^

for row in range(10):
  for col in range(10):
    if col == row + 0:
      print('^', end='')
    elif col == - row + 9:
      print('^', end='')
    else:
      print(' ', end='')
  print()
