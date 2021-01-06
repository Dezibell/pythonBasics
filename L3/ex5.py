#5
def sum_of_str(s: str) -> int:

    el = (int(el) for el in s.split(' ') if el!='/')
    return sum(el)

summary = 0
while True:
    s = input()
    try:
        s = s[:s.index('/')+1]
    except ValueError as e:
        s = s
    summary += sum_of_str(s)
    print(summary)
    if "/" in s:
        break
