# Задача 1:

# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = int(input()
res = 0

while n != 0:
    res += n%10
    n //= 10

print(res)