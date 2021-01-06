#5

from functools import reduce

ar = [el for el in range(100, 1001, 2)]
print(ar)
print(reduce((lambda a, b: a*b), ar))
