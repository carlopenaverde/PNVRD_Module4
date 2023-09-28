import math
import unittest

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert 7*7 == 49

def check(num):
    return num >= 49

class MyTest(unittest.TestCase):

    def test(self):
        self.assertTrue(check(7*7))

if __name__=='__main__':

    unittest.main()

  


