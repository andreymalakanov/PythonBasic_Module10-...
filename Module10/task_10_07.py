# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 7. Наибольшая сумма цифр')
print()
# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

print('Введите 0 для прерывания')
print()

n = -1
max_sum = 0
max_num = 0

while n != 0:
    num = n
    s = 0
    while n > 0:
      s += n % 10
      n //= 10
    if s > max_sum:
      max_sum = s
      max_num = num
    n = int(input('Введите число: '))

print('Число ', max_num, 'имеет макс-ую сумму цифр: ', max_sum)