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

