#1

def division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)

a = float(input())
b = float(input())
print(division(a, b))