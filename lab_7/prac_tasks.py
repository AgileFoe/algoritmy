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
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False
#8)
def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    
    current_max = max_element(arr, index + 1)
    
    if arr[index] > current_max:
        return arr[index]
    else:
        return current_max
#9)
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    else:
        return a * power(a, n - 1)
#10)
def count_depth(n, depth=0):
    if n == 0:
        return depth
    return count_depth(n - 1, depth + 1)