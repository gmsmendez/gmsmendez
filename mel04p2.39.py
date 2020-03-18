from abc import ABCMeta, abstractmethod
metaclass = ABCMeta
class Polygon(metaclass = ABCMeta):
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

class Triangle(metaclass=ABCMeta):
    def __init__(self, lengthofsides):
        polygon().__init__(self, 3, lengthofsides)
        self._area = self.area()
        self._perimetrer = self.perimeter()

    def area(self):
        return base*height/2

    def perimeter(self):
        return sum(self.lengthsides)

    class Quadrilateral(metaclass=ABCMeta):
        def __init__(self, lengthofsides):
            polygon.__init__(self, 4, [lengthofsides[0], lengthofsides[1], lengthofsides[0], lengthofsides[1]])

        def area(self):
            a, b = self.lengthofsides[0], self.lengthofsides[1]
            return a * b

        def perimeter(self):
            a, b = self.lengthofsides
            return (a + b) * 2

    class Pentagon(metaclass=ABCMeta):
        def __init__(self, lengthofsides):
            polygon.__init__(self, 5, lengthofsides)

        def area(self):
            x, y = self.lengthofsides[0], self.lengthofsides[1]
            return x * y

        def perimeter(self):
            x, y = self.lengthofsides
            return (x + y) * 2

    class Hexagon(metaclass=ABCMeta):
        def __init__(self, lengthofsides):
            polygon.__init__(self, 6, lengthofsides)

        def area(self):
            a, b = self.lengthofsides[0], self.lengthofsides[1]
            return a * b

        def perimeter(self):
            a, b = self.lengthofsides
            return (a + b) * 2

    class Octagon(metaclass=ABCMeta):
        def __init__(self, lengthofsides):
            polygon.__init__(self, 8, lengthofsides)

        def area(self):
            x, y = self.lengthofsides[0], self.lengthofsides[1]
            return x * y

        def perimeter(self):
            x, y = self.lengthofsides
            return (x + y) * 2