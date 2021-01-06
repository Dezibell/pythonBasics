#7

def fact(n: int):
    prev = 1
    for el in range(1, n+1):
        prev *= el
        yield prev


for el in fact(5):
    print(f"{el}!", end=' ', )
