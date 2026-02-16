numbers = [42, 7, 89, 13, 56]
second = 0
x = 0

if len(numbers) > 2:
    for i in numbers:
        if i > x:
            x = i

    numbers.remove(x)
    for i in numbers:
        if i > second:
             second = i 
    
else:
    print("список должен исеть больше 2-х значений")


print(second)