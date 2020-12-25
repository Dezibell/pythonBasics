#4
s = input('Введит строку из нескольких слов: ')
a = s.split(' ')
for el in enumerate(a):
    print(str(el[0])+': '+el[1][:10])