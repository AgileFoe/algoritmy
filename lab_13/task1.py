# 4.Суммирование элементов: Сравните время вычисления суммы чисел от 1 до $n$ через цикл и через формулу арифметической прогрессии.

import time

def sum_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_formula(n):
    return n * (n + 1) // 2

n = 10000000

# Через цикл
start = time.time()
sum_loop(n)
end = time.time()
print("Цикл:", end - start, "секунд")

# Через формулу S=n⋅(n+1)/2
start = time.time()
sum_formula(n)
end = time.time()
print("Формула:", end - start, "секунд")