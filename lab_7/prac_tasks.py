# 1)
def average(a, b, c):
    return (a + b + c) / 3

print(average(2, 2, 5))
# 2)
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(8))
# 3)
def power(a, n=2):
    return a ** n

print(power(5))
# 4)
def summ(*args):
    x = 0
    for i in args:
        x += i
    return x

print(summ(5, 10, 15, 20))
# 5)
def rec_nums(n):
    if n <= 0:
        return
    a = " "
    print(n, end=" ")
    rec_nums(n - 1)

rec_nums(9)
# 6)
def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(f"\n{sum_digits(255)}")
# 7)