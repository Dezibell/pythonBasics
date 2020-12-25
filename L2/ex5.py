#5
my_list = [7, 5, 3, 3, 2]
n = int(input('Введите число: '))
for i in range(len(my_list)-1, 0,-1):
    if my_list[i] >= n:
        my_list.insert(i+1, n)
        break
if not n in my_list:
    my_list.insert(0, n)
print(f'Пользователь ввёл число {n}. Результат: {my_list}')