import unittest
from app.models.board_property import Board_Property

class TestClass(unittest.TestCase):
  def setUp(self) -> None:
    """Set up an instance before each test"""
    self.property = Board_Property("Chef Lagenda", "property", 4, "red")  

  def test_initialization(self):
    """Test that Board_Property initlializes correctly."""
    self.assertEqual(self.property.name, "Chef Lagenda")
    self.assertEqual(self.property.price, 4)
    self.assertEqual(self.property.colour, "red")
    self.assertEqual(self.property.type, "property")
    self.assertEqual(self.property.rent, 4) # Rent should match the price initially
    self.assertEqual(self.property.owner, None)
    
    
  def test_duplicate(self):
    """Test that the duplicat_rent method correctly doubles the rent"""
    self.assertEqual(self.property.duplicate_rent(), 8)
      
if __name__ == '__main__':
    unittest.main()