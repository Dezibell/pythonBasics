#6_2

from itertools import cycle


iterator = lambda x: (el for el in cycle(x))
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
i = iterator(lst)
for el in range(0, 100):
    print(next(i), end=' ')
