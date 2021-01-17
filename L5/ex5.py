#4

nums = []
s = ''
while True:
    s = input('Введите число для записи в файл: ')
    if s == '':
        break
    nums.append(int(s))
try:
    with open('data2.txt', 'w') as f_obj:
        for el in nums:
            print(f'{el} ', file=f_obj)
    nums = []
    s = ''
    input('Нажмите enter для вычисления.')
    with open('data2.txt', 'r') as f_obj:
        s = f_obj.read()
    nums = [int(el) for el in s.split()]
    print(sum(nums))
except IOError:
    print('Ты хочешь файлы, а они тебя не хотят.')