# 7.Вложенные циклы II: Проанализируйте цикл, где итератор увеличивается в 2 раза на каждом шаге (i *= 2). Выведите логарифмическую сложность $O(\log n)$

import math

def log_cycle_iterations(n):
    i = 1
    count = 0
    while i <= n:
        count += 1
        i *= 2
    return count

# Пример использования
n = 123
iterations = log_cycle_iterations(n)
print(f"Количество итераций цикла для n = {n}: {iterations}")

# Проверка с формулой log2
log_approx = math.floor(math.log2(n)) + 1
print(f"Приблизительное количество итераций (log2(n) + 1): {log_approx}")