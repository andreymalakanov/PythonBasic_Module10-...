

# Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.



seqNum = int(input('Введите Кол-во чисел: '))
numeral = int(input('Введите цифру для подсчета: '))
while numeral < 0 or numeral > 9:
  numeral = int(input('Не верный ввод. Введите цифру для подсчета  в диапозоне от 0 до 9: '))
numCount = 0
for num in range(seqNum):
  number = int(input(f'Введите {num + 1}-е число: '))
  while number > 0:
    if number % 10 == numeral:
      numCount += 1
    number //= 10

print(f'Цифр {numeral} в последовательности: {numCount}')
  
print('\n' * 5 + '=' * 30, '\n')
