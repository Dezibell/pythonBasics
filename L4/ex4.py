#4

ar = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = []
g = (el for el in ar if el not in res)
for el in g:
    res.append(el)
print(res)
