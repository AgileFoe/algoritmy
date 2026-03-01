def sum_digits(n):
    n = abs(n)  # на случай отрицательных чисел
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def sum_d(n):
    x = 0
    for i in str(n):
        x += int(i)
        
    print(x)
    
print(sum_digits(1555))

sum_d(1555)