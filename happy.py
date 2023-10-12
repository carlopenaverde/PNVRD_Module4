import unittest

def name():
    name = 'HAPPY'
    return name

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(name(),'HAPPY')

if __name__=='__main__':

    unittest.main()
