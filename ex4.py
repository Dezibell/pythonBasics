#4
N = input('Enter any number: ')
i = 0
res = 0
while i<len(N):
    j = int(N[i])
    if j > res:
        res = j
    i += 1
print(res)