#3 with list
months = [
    'зима',
    'весна',
    'лето',
    'осень',
    'Мартобря 86 числа, между днём и ночью'
]
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
n = int(input('Введите номер месяца: '))
if n in winter:
    n = 0
elif n in spring:
    n = 1
elif n in summer:
    n = 2
elif n in autumn:
    n = 3
else:
    n = 4
print(months[n])

#3 with dict
monDict = {
    '1 2 12' : 'зима',
    '3 4 5'  : 'весна',
    '6 7 8'  : 'лето',
    '9 10 11': 'осень',
}
n = input('Введите номер месяца: ')
for el in monDict.keys():
    if n in el.split(' '):
        print(monDict[el])

