# Andrey Malakanov
# Skillbox PythonBasic

# Practice 10.4 - 1 

print('Задача 1. Электронная очередь')
print()

# Нам дали заказ написать программу для электронной очереди. У каждого человека в очереди есть номер: нулевой, первый, второй, третий и так далее. Каждый час очередь уменьшается на одного человека, то есть уходит сначала нулевой номер, затем первый, второй и так далее. Наша программа получает на вход одно число — количество людей в очереди — и выводит на экран историю обслуживания очереди: какие номера в какой час оставались.

people = int(input('Введите количесто людей: '))
for hour in range(people + 1):
  print('Идет час', hour)
  for num in range(hour, people):
    print('Номер в очереди', num)
  print()

print('\n' * 5 + '=' * 30, '\n')

# Practice 10.4 - 2 

print('Задача 2. Цифры больше пяти')
print()

# Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.

N = int(input("Введите количество чисел в последовательности: "))
count = 0
for num in range(N):
    new_number = int(input("Введите число: "))
    if new_number > 5:
      count += 1  
print("Ответ:", count)

# print(f'Цифр {numeral} в последовательности: {numCount}')
  
print('\n' * 5 + '=' * 30, '\n')


# Practice 10.4 - 2 

print('Задача 3. Лестница чисел')
print()

# Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:

N = int(input("Введите количество чисел в последовательности: "))

for start in range(N + 1):
    for number in range(start, N + 1):
        print(number, end='\t')
    print()




