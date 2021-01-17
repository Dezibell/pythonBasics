#2

rows = 0
words = 0
try:
    with open('data1.txt', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        rows = len(content)
        for el in content:
            words += len(el.split())
except IOError:
    print('Ошибка чтения файла')
print(f'В файле {rows} строк и {words} слов')
