score = int(input("введите оценку:"))
if 0 < score < 100:
    if score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("F")
else:
    print("введите оценку по 100 бальной системе")