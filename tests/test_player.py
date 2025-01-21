import unittest
from app.models.player import Player

class TestClass(unittest.TestCase):
  def setUp(self) -> None:
    """Set up an instance before each test"""
    self.player = Player("Alex")  

  def test_initialization(self):
    """Test that player initializes correctly."""
    self.assertEqual(self.player.name, "Alex")
    self.assertEqual(self.player.wallet, 16)
    self.assertEqual(self.player.location, 0)
    self.assertEqual(self.player.realestate, [])
    
    
  def test_credit(self):
    """Test that credit increases the rent"""
    self.assertEqual(self.player.credit(4), 20)
    
  def test_debit(self):
    """Test that credit increases the rent"""
    self.assertEqual(self.player.debit(4), 12)
    
  def test_set_location(self):
    """Test that the location is being set right when the dice is rolled"""
    self.assertEqual(self.player.set_location(5), 5)
  
  def test_set_location(self):
    """Test that the location is being set right when the dice is rolled"""
    self.assertEqual(self.player.set_location(7), None)
  
  def test_new_location(self):
    """Test that the realestate portfolio is growing"""
    self.assertEqual(self.player.new_realestate("RMIT"), ["RMIT"] )
    
  
if __name__ == '__main__':
    unittest.main()