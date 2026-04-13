# 11.Числа Фибоначчи: Сравните наивную рекурсию ($O(2^n)$) и итеративный подход ($O(n)$). Замерьте, при каком $n$ рекурсия «зависает».

import time

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


n_values = [10, 20, 30, 35, 40]  # n для теста

for n in n_values:
    start = time.time()
    fib_iterative(n)
    end = time.time()
    print(f"Итеративно n={n}: {end-start:.6f} секунд")
    
print("")

for n in n_values:
    start = time.time()
    fib_recursive(n)
    end = time.time()
    print(f"Рекурсивно n={n}: {end-start:.6f} секунд")