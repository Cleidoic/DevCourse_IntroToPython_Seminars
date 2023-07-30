# Задача 1:

# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))

def f(a, b):
  # базовый случай: если b равно 0, то возвращаем 1
  if b == 0:
    return 1
  # рекурсивный случай: если b больше 0, то возвращаем a умноженное на f(a, b-1)
  elif b > 0:
    return a * f(a, b-1)
  # иначе, если b меньше 0, то возвращаем 1 делить на f(a, -b)
  else:
    return 1 / f(a, -b)

print(f(a, b))

# *********************************************************************************

# В автотесте второй задачи ошибка. Ожидаемый ответ в автотесте не сумма двух чисел, а число b

# Задача 2:

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def sum(a, b):
  # базовый случай
  if a == 0:
    return b
  # рекурсивный случай
  return sum(a - 1, b + 1)

print(sum(a, b))
