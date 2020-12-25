#2
a = []
inp = ' '
i = 0
print('Enter \'\' to stop.')
while True:
    inp = input(f'Enter {(i+1)} element: ')
    if inp == '':
        break
    a.append(inp)
    i += 1
print(a)
i = 0
for i in range(0, len(a)-1, 2):
    if i < (len(a)):
        a[i], a[i+1] = a[i+1], a[i]
print(a)
