def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 0


for x in fibonacci_generator():
    count += 1
    if count == 5:
        print("Пятое число Фибоначчи:", x)
    elif count == 200:
        print("Двухсотое число Фибоначчи:", x)
    elif count == 1000:
        print("Тысячное число Фибоначчи:", x)
    elif count == 100000:
        print("Стотысячное число Фибоначчи:", x)
        break
