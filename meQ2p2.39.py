"""Gabriela Marie S. Mendez
   DATALGO Quiz 02
   Feb. 18, 2020
   I have neither received nor provided any help
   on this (lab) activity, nor have I concealed
   any violation of the Honor Code.
"""
from abc import ABCMeta, abstractmethod
class Pentagon(metaclass = ABCMeta):
    def __init__(self, lengthofsides):
        self.numberofsides = len(lengthofsides)
        self.lengthofsides = [0] * [self.numberofsides]
        assigned_values (self, lengthofsides)
    def print_numsides (self):
        print ('There are ' + str(self.numberofsides) + 'sides.')
    def assigned_values (self, lengthofsides):
        index = 0
        while index < len(lengthofsides):
            self.lengthofsides[index] = lengthofsides[index]
            index += 1

class Pentagon(metaclass=ABCMeta):
    def __init__(self, lengthofsides):
        Pentagon().__init__(self, 5, lengthofsides)
        self._area = self.area()
        self._perimeter = self.perimeter()

    def area(self):
        return (p) * (a) / 2

    def perimeter(self):
        return sum(self.lengthsides)

class Hexagon(metaclass=ABCMeta):
    def __init__(self, lengthofsides):
        hexagon().__init__(self, 6, lengthofsides)
        self._area = self.area()
        self._perimeter = self.perimeter()

    def area(self):
        return (3 sqrt(3) / 2) * (a**2)

    def perimeter(self):
        return sum(self.lengthsides)