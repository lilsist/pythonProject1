# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
# print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

 #1.Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

   """ time = int(input('введите число'))
    print('duration =', time)
    if time < 60:
        print(time, 'сек')
    elif time >= 60 and time < 3600:
        print(time // 60, 'мин', time % 60, 'сек')
    elif time >= 3600 and time < 86400:
        print(time // 3600, 'час', time % 3600 // 60, 'мин', time % 3600 % 60, 'сек')
    elif time > 86400:
        print(time // 86400, 'дн', time % 86400 // 3600, 'час', time % 3600 // 60, 'мин', time % 3600 % 60, 'сек' )
    else:
        print('что-то пошло не так :(') """

    # 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X).
    # Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

   """ list_for_cubes = []

    for i in range(1000):
        if i % 2 == 1:
            list_for_cubes.append(i ** 3)
    print(list_for_cubes)

    def sum_of_digits(num):
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits

    sum_from_loop = 0
    for g in list_for_cubes:
        a = sum_of_digits(g)
        if a % 7 == 0:
            sum_from_loop += g
    print(sum_from_loop)

    sum_from_loop1 = 0
    for g in list_for_cubes:
        g = g + 17
        b = sum_of_digits(g)
        if b % 7 == 0:
            sum_from_loop1 += g
    print(sum_from_loop1)
"""
# 3. Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой
# для каждого из чисел в интервале от 1 до 100:

list_precent = list(range(1, 101))

for i in list_precent:
    if i // 10 == 1:
        print(i, 'процентов')
    elif i % 10 == 0 or i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, 'процента')
  
