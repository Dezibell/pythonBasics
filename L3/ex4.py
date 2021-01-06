#4

def my_func(x: int, y: int) -> float:
    x = abs(x)
    y = -abs(y)
    return x ** y

def my_func1(x: int, y: int) -> float:
    x = abs(x)
    y = abs(y)
    res = x
    for el in range(y+1):
        res /= x
    return res

x = int(input())
y = int(input())
print(my_func(x, y))
print(my_func1(x, y))

