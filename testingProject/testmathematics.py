import unittest

from main import result
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.math = Mathematics()

    def test_add(self):
        result = self.math.sumToNUmbers(10, 5)
        self.assertEqual(result, 15)

    def test_multiply(self): #fonksiyonun ismi kesinlikle test kelimesiyle başlamalıdır.

        self.assertEqual(10, 10) #yazılan iki değer birbirine eşit mi bunu test ederiz.

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
