from lib import Circle, Triangle, Shape

import unittest


class Test(unittest.TestCase):
    def test_circle(self):
        circle1 = Circle(3)
        result = circle1.calc()
        self.assertEqual(result, 28.274)

    def test_triangle(self):
        triangle1 = Triangle(2,3,4)
        result = triangle1.calc()
        self.assertEqual(result, 2.905)

    def test_is_rect(self):
        triangle2 = Triangle(2,3,4)
        triangle3 = Triangle(3,4,5)
        result2 = triangle2.isRight
        result3 = triangle3.isRight
        self.assertEqual(result2, False)
        self.assertEqual(result3, True)

    def test_is_correct(self):
        with self.assertRaises(ValueError):
            triangle4 = Triangle(-2, 3, 4)
            result4 = triangle4.calc()

