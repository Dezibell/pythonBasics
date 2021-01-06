#2

def show_info(name, second_name, year, city='Moscow', email='', phone=0):
    print(f'Name: {name}, '
          f'second name: {second_name}, '
          f'year of birth: {year}, '
          f'lives in city: {city}, '
          f'email: {email}, '
          f'phone number: {phone}')

show_info(name = 'Denis',
          second_name='Nefedov',
          year=1993,
          email='dez4minds@mail.ru',
          phone=89999999999)