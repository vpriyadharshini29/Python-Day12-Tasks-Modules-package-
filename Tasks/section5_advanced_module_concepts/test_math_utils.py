import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

if __name__ == "__main__":
    unittest.main()
