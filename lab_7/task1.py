def add(a, b):
    return a + b

def power(a, n=2):
    return a ** n

def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total

print(add(10, 5))
print(power(9))
print(add(10, 45))