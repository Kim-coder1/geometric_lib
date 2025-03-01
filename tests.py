import unittest
import math

import circle 
import rectangle 
import triangle 
import square 

class TestGeometryFunctions(unittest.TestCase):

    
    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 5 * 5)
    
    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(10, 5), 10 * 5)
    
    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(10, 5), 2 * (10 + 5))

    
    def test_triangle_area(self):
        self.assertEqual(triangle.area(10, 5), 10 * 5 / 2)
    
    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 3 + 4 + 5)

    
    def test_square_area(self):
        self.assertEqual(square.area(4), 4 * 4)
    
    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(4), 4 * 4)

if __name__ == '__main__':
    unittest.main()
