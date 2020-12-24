#3
n = input('Enter a number: n = ')
print(f'n + nn + nnn = {n} + {f"{n}{n}"} + {f"{n}{n}{n}"} = '
      f'{str(int(n)+int(f"{n}{n}")+int(f"{n}{n}{n}"))}')
