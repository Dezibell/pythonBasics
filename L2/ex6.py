#6
products = []
keys = (
    ('название', False),
    ('цена', True),
    ('количество', True),
    ('ед', False),
)
sum = dict()
a = ''
for i in range(3):
    for el in keys:
        a = input(f'Введите {el[0]}: ')
        sum[el[0]] = int(a) if el[1] else a
    products.append((i+1, sum.copy()))
print(products)
for el in keys:
    sum[el[0]] = []
    for el_ in products:
        if not el_[1][el[0]] in sum[el[0]]:
            sum[el[0]].append(el_[1][el[0]])
print(sum)