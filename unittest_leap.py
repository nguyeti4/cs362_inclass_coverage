import unittest
import leap2

class Testleap(unittest.TestCase):
    def test_leap(self):
        actual = leap2.leap("500")
        expected = "500 is not a leap year"
        self.assertEqual(actual,expected)
    def test_leap2(self):
        actual = leap2.leap("400")
        expected = "400 is a leap year"
        self.assertEqual(actual,expected)
    def test_leap3(self):
        actual = leap2.leap("-100")
        expected = "error: input needs to be a POSITIVE int"
        self.assertEqual(actual,expected)
        
