#3
from sys import exit

content = []
try:
    with open('EmployeesList.txt', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
except IOError as e:
    print('Неудачник здесь ты.')
    exit(e)

pay = [float(el.split()[1]) for el in content]
loosers = [el.split()[0] for el in content if float(el.split()[1]) < 20000]
m_pay = sum(pay) / len(pay)

print('Список неудачников:')
print(loosers)
print(f'Средняя зарплата: {m_pay:.1f}')
