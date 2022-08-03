# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 5. Простые числа')

#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

print('Задача 5. Простые числа')

numbers = int(input('Введите кол-во проверяемых чисел: '))
counter = 0

for num1 in range(1, numbers + 1):
  flag = True
  number = int(input('Введите число: '))
  for num2 in range(2, number):
    if number %  num2 == 0:
      flag = False  
  if flag:
    counter += 1
    
print('Кол-во простых чисел в последовательности:', counter)
