#4

class Car:
    _speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed: int, color: str, name: str):
        self._speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина едет')

    def stop(self):
        print("Машина стоит")

    def turn(self, direction: bool):
        print(f'Машина повернула {"направо" if direction else "налево"}')

    def show_speed(self) -> int:
        return self._speed


class TownCar(Car):
    def show_speed(self) -> int:
        if self._speed > 60:
            print('Потише, дома тебя ждут.')
        return super().show_speed()


class WorkCar(Car):
    def show_speed(self) -> int:
        if self._speed > 40:
            print('Ты как-то слишком торопишься на работу.')
        return super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed: int, name: str):
        super().__init__(speed, 'цвет справедливости', name)
        self.is_police = True


tc = TownCar(62, 'green', 'mazda')
wc = WorkCar(50, 'red', 'volkswagen')
sc = SportCar(100, 'black', 'ferrari')
pc = PoliceCar(80, 'lada')

print(tc.name)
print(tc.color)
print(tc.show_speed())
tc.go()
tc.stop()
tc.turn(True)
tc.turn(False)
print(wc.name)
print(wc.color)
print(wc.show_speed())
print(sc.name)
print(sc.color)
print(sc.show_speed())
print(pc.name)
print(pc.color)
print(pc.show_speed())
if pc.is_police:
    print('Едем ловить негодяев!')
