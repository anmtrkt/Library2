from math import pi, sqrt, isfinite

class Shape:
    def calc(self):
        pass
class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

        self.area = None

    def calc(self):
        if self.area is None:
            self.area = pow(self.rad,2) * pi
            area = round(self.area,3)
            print(area)
            return area

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not (isfinite(side1) and side1 > 0):
            raise ValueError("Должно быть положительное число: side1")
        if not (isfinite(side2) and side2 > 0):
            raise ValueError("Должно быть положительное число: side2")
        if not (isfinite(side3) and side3 > 0):
            raise ValueError("Должно быть положительное число: side3")

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        self.area = None
        self.is_right = None

    def calc(self):
        if self.area is None:
            perim = (self.side1 + self.side2 + self.side3) / 2
            self.area = sqrt(
                perim
                * (perim - self.side1)
                * (perim - self.side2)
                * (perim - self.side3)
            )
            area = round(self.area, 3)
            print(area)
        return area


    @property
    def isRight(self):

        if self.is_right is None:
            a, b, c = self.side1, self.side2, self.side3
            if c < b:
                c, b = b, c
            if c < a:
                c, a = a, c
            self.is_right = pow(c,2) == pow(b,2) + pow(a,2)
        print(self.is_right)
        return self.is_right


