#4
nums = { 'One': 'Один',
         'Two': 'Два',
         'Three': 'Три',
         'Four': 'Четыре',
         }
try:
    with open('numbers.txt', 'r', encoding='utf-8') as f_obj:
        r_content = f_obj.readlines()
        w_content = ''
        for el in r_content:
            s = el.split()
            s[0] = nums[s[0]]
            w_content += ' '.join(s)+'\n'
    with open('translatedNumbers.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.writelines(w_content)
except IOError:
    print('Траблы с файлом')
