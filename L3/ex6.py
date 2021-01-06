#5

def int_func(s: str) -> str:
    s.strip()
    if s[0].islower():
        s = s[0].upper() + s[1:]
    return s

s = input('Enter any word: ')
print(int_func(s))
s = input('Enter some words: ')
lst = s.split(' ')
lst_ = []
for el in lst:
    lst_.append(int_func(el))
print(lst_)