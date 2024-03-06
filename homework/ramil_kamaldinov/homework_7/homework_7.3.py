r1 = 'результат операции: 42'
r2 = 'результат операции: 54'
r3 = 'результат работы программы: 209'
r4 = 'результат: 2'

r11 = int(r1[r1.index(':') + 2:])
r22 = int(r2[r2.index(':') + 2:])
r33 = int(r3[r3.index(':') + 2:])
r44 = int(r4[r4.index(':') + 2:])


def summ(numb):
    print(numb + 10)


summ(r11)
summ(r22)
summ(r33)
summ(r44)
