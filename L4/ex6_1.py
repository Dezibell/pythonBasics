#6_1

from itertools import count


def iterator(n: int):
    for el in count(n):
        if el > 10:
            break
        else:
            yield el


i = iterator(3)
while True:
    try:
        print(next(i))
    except StopIteration as e:
        break
