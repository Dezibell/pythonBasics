#1
integer1 = 0
integer2 = 0
string = ''
integer1 = int(input('input a number: '))
integer2 = int(input('input another number: '))
string = input('input a string: ')
print(f'integer = {integer1}')
print(f'another integer = {integer2}')
print(f'string = {string}')
print(f'sum with string: {str(integer1+integer2) + string}')