#6
table = {}
try:
    with open('shedule.txt', 'r', encoding='utf-8') as f_obj:
        text = f_obj.readlines()
        for row in text:
            key, hours = row.split(':')[0], row.split(':')[1]
            num = ''
            num_list = []
            for char in hours:
                if char.isdigit():
                    num += char
                elif num != '':
                    num_list.append(int(num))
                    num = ''
            table[key] = sum(num_list)
except IOError as e:
    print(e)

print(table)