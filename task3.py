# Створіть інженерний калькулятор з використанням модуля math,
# в якому передбачене меню. Під час створення дотримуйтесь
# правил специфікації PEP 8.

import math


def menu(n):
    while True:
        print(
            'Список операцій: \n1.Додавання \n2.Віднімання \n3.Множення \n4.Ділення '
            '\n5.Зведення в ступінь \n6.Квадратний корінь'
            '\n7.Кубічний корінь \n8.Косінус \n9.Синус \n10.Тангенс '
            '\n11.Арккосинус \n12.Арксинус \n13.Арктангенс \n14.Логарифм \n15.Вихід')
        n = int(input('Введи цифру операції, яку потрібно виконати (без точки): '))
        if n == 1:
            print('Операція додавання')
            plus(int(input('Введи перший доданок: ')), int(input('Введи другий доданок: ')))
        elif n == 2:
            print('Операція віднімання')
            minus(int(input('Введи зменшуване число: ')), int(input("Введи від'ємник: ")))
        elif n == 3:
            print('Операція множення')
            multi(int(input('Введи перший множник: ')), int(input('Введи другий множник: ')))
        elif n == 4:
            print('Операція ділення')
            divi(int(input('Введи дільне: ')), int(input('Введи дільник: ')))
        elif n == 5:
            print('Операція зведення у ступінь')
            expo(int(input('Введи число, яке треба звести у ступінь: ')),
                 int(input('Введи ступінь, у яку треба звести: ')))
        elif n == 6:
            print('Операція зведення до квадратного кореня')
            sqrt(int(input('Введи число, квадратний корінь якого хочеш знайти: ')))
        elif n == 7:
            print('Операція зведення до кубічного кореня')
            sqrt(int(input('Введи число, кубічний корінь якого хочеш знайти: ')))
        elif n == 8:
            print('Операція знаходження косінуса')
            cos(int(input('Введи число, косінус якого хочеш знайти: ')))
        elif n == 9:
            print('Операція знаходження синуса')
            sin(int(input('Введи число, синус якого хочеш знайти: ')))
        elif n == 10:
            print('Операція знаходження тангенса')
            tg(int(input('Введи число, тангенс якого хочеш знайти: ')))
        elif n == 11:
            print('Операція знаходження арккосінуса')
            acos(int(input('Введи число, арккосінус якого хочеш знайти: ')))
        elif n == 12:
            print('Операція знаходження арксінуса')
            asin(int(input('Введи число, арксінус якого хочеш знайти: ')))
        elif n == 13:
            print('Операція знаходження арктангенса')
            atg(int(input('Введи число, арктангенс якого хочеш знайти: ')))
        elif n == 14:
            print('Операція знаходження логарифма')
            log(int(input('Введи число, логарифм якого хочеш знайти: ')), int(input('Введи базу логарифму: ')))
        elif n == 15:
            break


def plus(a, b):
    print(f'Результат додавання {a} до {b} дорівнює {a + b}')


def minus(a, b):
    print(f'Результат віднімання {a} віл {b} дорівнює {a - b}')


def multi(a, b):
    print(f'Результат множення {a} на {b} дорівнює {a * b}')


def divi(a, b):
    if b != 0:
        print(f'Результат ділення {a} на {b} дорівнює {a / b}')
    else:
        print("Ви намагаєтесь поділити на нуль.")


def expo(a, b):
    print(f'Результат зведення {a} у ступінь {b} дорівнює {a ** b}')


def sqrt(a):
    if a < 0:
        print(f"Квадратний корінь числа {a} дорівнює {math.sqrt(abs(a)) * -1}")
    elif a > 0:
        print(f"Квадратний корінь числа {a} дорівнює {math.sqrt(a)}")


def sqrt3(a):
    if a < 0:
        print(f"Кубічний корінь числа {a} дорівнює {(abs(a) ** (1 / 3)) * -1}")
    elif a > 0:
        print(f"Кубічний корінь числа {a} дорівнює {a ** (1 / 3)}")


def acos(a):
    print(f"Арккосинус корінь числа {a} дорівнює {math.acos(a)}")


def asin(a):
    print(f"Арксінус корінь числа {a} дорівнює {math.asin(a)}")


def atg(a):
    print(f"Арктангенс корінь числа {a} дорівнює {math.atan(a)}")


def cos(a):
    print(f"Косінус корінь числа {a} дорівнює {math.cos(a)}")


def sin(a):
    print(f"Сінус корінь числа {a} дорівнює {math.sin(a)}")


def tg(a):
    print(f"Тангенс корінь числа {a} дорівнює {math.tan(a)}")


def log(a, b):
    print(f"Логарфм числа {a} по базі {b} дорівнює {math.log(a, b)}")


print('some_change')
menu(None)
