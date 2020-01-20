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

class Testing(unittest.TestCase):
    def test_add(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c = a + b
        z = VectorCount(7.0, 7.0, 5.0)
        self.assertEqual(c, z)

    def test_mul(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c = a * b
        z = VectorCount(26)
        self.assertEqual(c, z)

    def test_sub(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c = a - b
        d = VectorCount(-3, -1, 3)

    def test_numeral_mul(self):
        a = VectorCount(2, 3, 4)
        b = 2.5
        c = a * b
        z = VectorCount(5, 7.5, 10)
        self.assertEqual(c, z)

    def test_float(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c = float(a)
        d = float(b)
        c1 = 5.39
        c2 = 6.48
        self.assertEqual(c, c1)
        self.assertEqual(d, c2)

    def test_vect_mul(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c = VectorCount.vect_mul(a, b)
        c1 = VectorCount(-13, 18, -7)
        self.assertEqual(c, c1)

    def test_angle(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c5 = VectorCount.angle_vectors(a, b)
        c6 = 41.84
        self.assertEqual(c5, c6)

    def test_col(self):
        a = VectorCount(2, 3, 4)
        b = VectorCount(5, 4, 1)
        c = VectorCount.collin(a, b)
        c1 = False
        self.assertEqual(c, c1)

if __name__ == '__main__':
    unittest.main()
