def rec_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * rec_factorial(num - 1)

print(rec_factorial(6))

def factorial(num):
    x = 1
    for i in range(1, num + 1):
        y = x
        x = i * x
        print(f"{i} * {y} = {x}")
    print(f"результат !{num}:", x)

factorial(7)