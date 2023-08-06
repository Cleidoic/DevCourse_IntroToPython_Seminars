# Задача 1:  

# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Каждое число вводится с новой строки.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))

def arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression

print(arithmetic_progression(a1, d, n))

# *********************************************************************************

# Задача 2: 

# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def find_i_in_range(arr, min_v, max_v):
    indices = []
    for i, value in enumerate(arr):
        if min_v <= value <= max_v:
            indices.append(i)
    return indices

my_list = [random.randint(1, 100) for i in range(int(input('Введите количество елементов массива: ')))]
min_v = int(input('Введите нижнюю границу диапазона: '))
max_v = int(input('Введите верхнюю границу диапазона: '))
result = find_i_in_range(my_list, min_v, max_v)

print(f'Исходный список: {my_list}')
print(f'Индексы элементов, значения которых находятся в диапазоне от, {min_v} до {max_v}: {result}')
