massage = "global" # глобальная переменная

def func():
    massage = "local" # локальная переменная
    print(massage)

print(massage) # вывод глобальной переменной

func() # вывод локальной переменной внутри функции