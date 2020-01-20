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
