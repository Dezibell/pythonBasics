#1

with open('outputData.txt', 'w') as f_obj:
    while True:
        s = input()
        if s != '':
            print(s, file=f_obj)
        else:
            break
