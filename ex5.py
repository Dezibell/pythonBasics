#5
a = int(input('Введите сумму выручки: '))
b = int(input('Введите сумму издержек: '))
if a>b:
    print('Ваша фирма работала с прибылью = '+str(a-b))
    print('Рентабельность = '+str((a-b)/a))
    h = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы в рассчёте на каждого сотрудника = '+str((a-b)/h))
else:
    print('Ваша фирма работает с убытком = '+str(a-b))