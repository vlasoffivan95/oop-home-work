from math import sqrt, acos, degrees
import unittest


class VectorCount(object):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    #в данной функции уже предусмотрено умножение вектора на вектор и на число
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return VectorCount(self.x*other, self.y*other, self.z*other)
        elif isinstance(other, VectorCount):
            return VectorCount(self.x * other.x + self.y * other.y + self.z * other.z)

    def __add__(self, other):
        return VectorCount(self.x+other.x, self.y+other.y, self.z + other.z)

    def __sub__(self, other):
        return VectorCount(self.x - other.x, self.y - other.y, self.z - other.z)

    # векторное произведение
    def vect_mul(self, other):
        return VectorCount((self.y * other.z - self.z * other.y), (self.z * other.x - self.x * other.z),
                           (self.x * other.y - self.y * other.x))

    def __float__(self):
        return round((sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)), 2)

    # функция для расчета угла между векторами
    def angle_vectors(self, other):
        angle = (degrees(acos((self.x * other.x + self.y * other.y + self.z * other.z) / (
                    (sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)) *
                    (sqrt(other.x ** 2 + other.y ** 2 + other.z ** 2))))))
        return round((angle), 2)

    def __repr__(self):
        return '%0.1f, %0.1f, %0.1f' % (self.x, self.y, self.z)

    def __str__(self):
        return self.__repr__()

    # функция для определения коллинеарности векторов
    def collin(self, other):
        if self.x / other.x == self.y / other.y == self.z / other.z:
            return True
        else:
            return False
