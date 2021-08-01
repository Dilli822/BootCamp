
import unittest

def add(x,y):
        return x+y

class Testing(unittest.TestCase):
  

    def test_positive(self):
        self.assertEqual(add(5,5), 10)

        def test_negative(self):
            self.assertNotEqual(add(5,5), 11)
            
            if __name__ == '__main__':
                unittest.main()



