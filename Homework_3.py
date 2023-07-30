# Задача 1:

# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

list_1 = [1, 2, 3, 4, 3]
k = 3

def count_num(list_1, k):
    return list_1.count(k)

print(count_num(list_1, k))

# Или циклом:

# def count_num(list_1, k):
#     count = 0
#     for num in list_1:
#         if num == k:
#             count += 1
#     return count

# *********************************************************************************

# Задача 2:

# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6

def find_closest_element(list_1, k):
    closest_element = min(list_1, key=lambda x: abs(x - k))
    return closest_element

print(find_closest_element(list_1, k))

# Или циклом:

# def find_closest_element(list_1, k):
#     closest_element = None
#     min_difference = float('inf')

#     for element in list_1:
#         difference = abs(element - k)
#         if difference < min_difference:
#             closest_element = element
#             min_difference = difference
#     return closest_element

# *********************************************************************************

# Задача 3:

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

k = input()

def scrabble_score(word):
    points = { 1: 'AEIOULNSTRАВЕИНОРСТ' , 2: 'DGДКЛМПУ' , 3: 'BCMPБГЁЬЯ' , 4: 'FHVWYЙЫ' , 5: 'KЖЗХЦЧ' , 8: 'JXШЭЮ' , 10: 'QZФЩЪ' }
    score = sum([k for i in word.upper() for k, v in points.items() if i in v])
    return score

print(scrabble_score(k))






