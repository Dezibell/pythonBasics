#2

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass_of_asphalt(self, mass, thickness):
        return self._width * self._length * mass * thickness


road = Road(20, 5000)
print(road.calculate_mass_of_asphalt(25, 5))

