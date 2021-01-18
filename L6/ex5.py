#5

class Stationery:
    title = ''

    def __init__(self):
        pass

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        title = 'pen'

    def draw(self):
        print('Рисуем ручкой.')


class Pencil(Stationery):
    def __init__(self):
        title = 'pencil'

    def draw(self):
        print('Рисуем карандашом.')


class Handle(Stationery):
    def __init__(self):
        title = 'handle'

    def draw(self):
        print('Рисуем маркером.')


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
