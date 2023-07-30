# Задача 1: 

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Импортируем модуль random для генерации случайных целых чисел
import random

# Вводим количество элементов первого и второго множеств
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Заполняем список set1 случайными целыми числами от 1 до 100 с помощью генератора списков
set1 = [random.randint(1, 100) for i in range(n)]

# Заполняем список set2
set2 = [random.randint(1, 100) for j in range(m)]

# Преобразуем списки во множества, чтобы избавиться от повторений
set1 = set(set1)
set2 = set(set2)

# Находим пересечение двух множеств - общие элементы
intersection = set1 & set2

# Преобразуем множество в список и сортируем его по возрастанию
intersection = list(intersection)
intersection.sort()

# Выводим результат
print("Числа, которые встречаются в обоих наборах:")
for number in intersection:
    print(number)

# *********************************************************************************

# Задача 2:

# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# Импортируем модуль random для генерации случайных чисел
import random

# Вводим число кустов на грядке
bushes = int(input("Введите число кустов на грядке: "))

# Генерируем случайное число ягод от 1 до 100 для каждого куста генератором списков
berries = [random.randint(1, 10) for i in range(bushes)]

# Проверяем количество ягод на кустах
print(berries)

# Создаем переменную для хранения максимального числа ягод, которое можно собрать за один заход
max_berries = 0

# Перебираем все возможные позиции собирающего модуля
for i in range(bushes):
    # Считаем сумму ягод на текущем кусте и двух соседних
    sum_berries = berries[i] + berries[(i - 1) % bushes] + berries[(i + 1) % bushes]
    # Если сумма больше максимальной, обновляем максимальную сумму
    if sum_berries > max_berries:
        max_berries = sum_berries

# Выводим максимальное число ягод, которое можно собрать за один заход
print("Максимальное число ягод, которое можно собрать за один заход: ", max_berries)
