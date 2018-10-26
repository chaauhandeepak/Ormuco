import unittest
from linesOverlap import OverLap

class TestsForOverLap(unittest.TestCase):

    # Test methods for Overlap Function of two lines on x-axis

    def test_PositiveInt_OverLap(self):
        result=OverLap((1,5),(3,6))
        self.assertEqual(result,'\n(1, 5) & (3, 6) overlaps on x-axis')

    def test_PositiveInt_NotOverLap(self):
        result=OverLap((1,5),(6,11))
        self.assertEqual(result,"\n(1, 5) & (6, 11) doesn\'t overlaps on x-axis")

    def test_NegitiveInt_OverLap(self):
        result=OverLap((-1,-5),(-3,-6))
        self.assertEqual(result,'\n(-1, -5) & (-3, -6) overlaps on x-axis')

    def test_NegitiveInt_NotOverLap(self):
        result=OverLap((-1,-5),(-6,-11))
        self.assertEqual(result,"\n(-1, -5) & (-6, -11) doesn\'t overlaps on x-axis")

    def test_Integers_OverLap(self):
        result=OverLap((-1,2),(0,-2))
        self.assertEqual(result,'\n(-1, 2) & (0, -2) overlaps on x-axis')

    def test_Origin_OverLap(self):
        result=OverLap((0,0),(0,0))
        self.assertEqual(result,'\n(0, 0) & (0, 0) overlaps on x-axis')

    def test_Integers_OverLaps(self):
        result=OverLap((-1,-3),(1,3))
        self.assertEqual(result,"\n(-1, -3) & (1, 3) doesn\'t overlaps on x-axis")

unittest.main()