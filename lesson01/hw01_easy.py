
__author__ = 'Нестеров Антон'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# код пишем тут...
>>> a = 189736487263
>>> for i in str(a):
	print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

    c = 0
    a = int(input('Введите число a:'))
    c = a
    b = int(input('Введите число b:'))
    a = b
    b = c
    print('a =', a, 'b =', b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
    a = int(input('Введите Ваш возраст:'))
    if a >= 18:
        print('Доступ разрешен')
    else:
        print('Извините, пользование данным ресурсом только с 18 лет')
    
