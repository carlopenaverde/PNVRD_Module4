import unittest

def check(num):
    return num >=100

class MyTest(unittest.TestCase):

    def test(self):
        self.assertTrue(check(100))

if __name__=='__main__':

    unittest.main()
