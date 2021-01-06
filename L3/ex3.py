def my_func(a, b, c):
    lst = sorted([a, b, c])
    return lst[1] + lst[2]

a = int(input())
b = int(input())
c = int(input())

print(my_func(a, b, c))