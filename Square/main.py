class Square:
    length = 0
    def __init__(self, length=0):
        if length > 0:
            self.length = length

    @property
    def _length(self):
        return self.length

    @_length.setter
    def _length(self, value):
        if value > 0:
            self.length = value
        else:
            raise ValueError("Сторона квадрата положительное число")

    @property
    def get_area(self):
        return self.length ** 2

    def __str__(self):
        return f"Длина = {self._length} м, Площадь фигуры = {self.get_area} кв.м"

