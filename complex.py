import unittest
import math


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"

    def phase(self):
        return math.atan2(self.imaginary, self.real)

    def log(self, base):
        return ComplexNumber(math.log(self.real) / math.log(base), self.phase() / math.log(base))

    def magnitude(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __eq__(self, other):
        return self.real == other.real  and self.imaginary == other.imaginary

    def isclose(self, c, delta):
        return math.sqrt((self.real-c.real)**2 + (self.imaginary-c.imaginary)**2) < delta

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real,self.imaginary + other.imaginary)
        elif type(other) is int or type(other) is float:
            return ComplexNumber(self.real + other, self.imaginary)
        else:
            return NotImplemented

    def __radd__(self, other):
        if (type(other) is int or type(other) is float):
            return ComplexNumber(self.real + other, self.imaginary)
        else:
            return NotImplemented

    def __mul__(self, other):

        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                                 self.imaginary * other.real + self.real * other.imaginary)
        elif type(other) is int or type(other) is float:
            return ComplexNumber(self.real * other, self.imaginary * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if (type(other) is int or type(other) is float):
            return ComplexNumber(self.real * other, self.imaginary * other)
        else:
            return NotImplemented


class ComplexNumberTest(unittest.TestCase):

    def test_01_init(self):
        self.assertEqual(ComplexNumber(1,2).real, 1)
        self.assertEqual(ComplexNumber(1,2).imaginary, 2)

    def test_02_phase(self):

        self.assertAlmostEqual(ComplexNumber(0.0,1.0).phase(), math.pi / 2, delta=0.001)

    def test_03_str(self):
        self.assertEqual(str(ComplexNumber(1,2)), "1 + 2i")
        #self.assertEqual(str(ComplexNumber(1,0)), "1")
        #self.assertEqual(str(ComplexNumber(1.0,0)), "1.0")
        #self.assertEqual(str(ComplexNumber(0,1)), "i")
        #self.assertEqual(str(ComplexNumber(0,0)), "0")

    def test_04_log(self):
        c = ComplexNumber(1.0,1.0)
        l = c.log(math.e)
        self.assertAlmostEqual(l.real, 0.0, delta=0.001)
        self.assertAlmostEqual(l.imaginary, c.phase(), delta=0.001)

    def test_05_magnitude(self):
        self.assertAlmostEqual(ComplexNumber(3.0,4.0).magnitude(),5, delta=0.001)

    def test_06_integer_equality(self):

        c = ComplexNumber(0,0)
        c.real = 1
        c.imaginary = 2
        self.assertEqual(c, ComplexNumber(1,2))

    def test_07_isclose(self):
        self.assertTrue(ComplexNumber(1.0,1.0).isclose(ComplexNumber(1.0,1.1), 0.2))
        self.assertFalse(ComplexNumber(1.0,1.0).isclose(ComplexNumber(10.0,10.0), 0.2))

    def test_08_add_zero(self):
        self.assertEqual(ComplexNumber(1,2) + ComplexNumber(0,0), ComplexNumber(1,2));

    def test_09_add_numbers(self):
        self.assertEqual(ComplexNumber(1,2) + ComplexNumber(3,4), ComplexNumber(4,6));

    def test_10_add_scalar_right(self):
        self.assertEqual(ComplexNumber(1,2) + 3, ComplexNumber(4,2));

    def test_11_add_scalar_left(self):
        self.assertEqual(3 + ComplexNumber(1,2), ComplexNumber(4,2));

    def test_12_add_negative(self):
        self.assertEqual(ComplexNumber(-1,0) + ComplexNumber(0,-1), ComplexNumber(-1,-1));

    def test_13_mul_by_zero(self):
        self.assertEqual(ComplexNumber(0,0) * ComplexNumber(1,2), ComplexNumber(0,0));

    def test_14_mul_just_real(self):
        self.assertEqual(ComplexNumber(1,0) * ComplexNumber(2,0), ComplexNumber(2,0));

    def test_15_mul_just_imaginary(self):
        self.assertEqual(ComplexNumber(0,1) * ComplexNumber(0,2), ComplexNumber(-2,0));

    def test_16_mul_scalar_right(self):
        self.assertEqual(ComplexNumber(1,2) * 3, ComplexNumber(3,6));

    def test_17_mul_scalar_left(self):
        self.assertEqual(3 * ComplexNumber(1,2), ComplexNumber(3,6));