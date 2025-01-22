import unittest
from math import ceil
from random import randint
from app.services.create_rounds import create_rounds


class TestClass(unittest.TestCase):
  def setUp(self):
    """Create two random lists to check if the split works"""
    n1 = randint(25, 50)
    n2 = randint(2, 9)
    self.list_1 = [randint(1, 6) for _ in range(n1)]
    self.list_2 = [randint(1,10) for _ in range(n2)]
    self.result = ceil(n1 / len(self.list_2))

    
  def test_list_len(self):
    """Test that the second list has the correct amount of splits"""
    self.assertEqual(len(create_rounds(self.list_1, self.list_2)), self.result)


if  __name__ == "__main__":
  unittest.main()