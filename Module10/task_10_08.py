# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.

# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

print()

hight = int(input('Введите высоту пирамиды: '))
hight *= 2

for row in range(1, hight + 1, 2):
    for col in range(1, row + 1):
        if row == col:
            print(' ' * (hight - 1) + '#' * col)
            hight -= 1