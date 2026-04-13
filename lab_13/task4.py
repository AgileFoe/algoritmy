# 17.Хеширование: Проанализируйте, как заполненность хеш-таблицы влияет на время поиска (средний случай против худшего).  

import random

def simulate_hash_search(n, m, trials=10000):
    # n - количество элементов
    # m - размер таблицы
    table = [[] for _ in range(m)]  # цепочки
    # случайные ключи
    for _ in range(n):
        key = random.randint(0, 10*n)
        table[key % m].append(key)
    
    # симуляция поиска
    checks = []
    for _ in range(trials):
        key = random.randint(0, 10*n)
        bucket = table[key % m]
        check = 0
        for k in bucket:
            check += 1
            if k == key:
                break
        checks.append(check)
    avg_checks = sum(checks)/len(checks)
    return avg_checks

for alpha in [0.1, 0.5, 0.9]:
    n = int(alpha*1000)
    m = 1000
    avg = simulate_hash_search(n, m)
    print(f"Load factor {alpha}: среднее число проверок ≈ {avg:.2f}")