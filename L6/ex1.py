#1
import time


class TrafficLight:
    __COLORS = (
        ('Красный', 7),
        ('Жёлтый', 2),
        ('Зелёный', 3),
    )
    __color = ''

    def __init__(self):
        pass

    def running(self):
        for el in TrafficLight.__COLORS:
            self.__color = el[0]
            print(self.__color)
            time.sleep(el[1])


tl = TrafficLight()
tl.running()
