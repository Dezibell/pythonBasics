#2

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res = [lst[i] for i in range(1, len(lst)) if lst[i]>lst[i-1]]
print(res)
