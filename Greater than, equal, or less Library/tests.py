import unittest
from module import ValueComparsions

class TestsForStrings(unittest.TestCase):

    def test1_ForGreater(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertEqual(Strings.Greater(),'1.3 is greater than 1.1')

    def test2_ForGreater(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertNotEqual(Strings.Greater(),'1.1 is greater than 1.3')

    def test3_ForGreater(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertTrue(Strings.Greater(),'1.3 is greater than 1.1')

    def test1_ForLesser(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertEqual(Strings.Lesser(),'1.1 is lesser than 1.3')

    def test2_ForLesser(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertNotEqual(Strings.Lesser(),'1.3 is lesser than 1.1')

    def test3_ForLesser(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertTrue(Strings.Lesser(),'1.1 is lesser than 1.3')


    def test1_ForEqual(self):
        Strings=ValueComparsions('1.1','1.3')
        self.assertEqual(Strings.Equal(),'1.1 not equal 1.3')

    def test2_ForEqual(self):
        Strings=ValueComparsions('1.1','1.1')
        self.assertEqual(Strings.Equal(),'1.1 is equal to 1.1')

    def test3_ForEqual(self):
        Strings=ValueComparsions('1.1','1.1')
        self.assertNotEqual(Strings.Equal(),'1.1 not equal 1.3')




unittest.main()