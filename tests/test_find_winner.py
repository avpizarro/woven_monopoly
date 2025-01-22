import unittest
from app.services.find_winner import find_winner
from app.models.player import Player

class TestClass(unittest.TestCase):
  def setUp(self):
    """Create test players before each test"""
    self.players = [
      Player("María"),
      Player("Aluna"),
      Player("Myriam"),
      Player("Alejandra")
    ]
  
  def test_unique_winner(self):
    """Test when there is only one winner"""
    self.players[1].credit(10)
    self.players[3].debit(16)
    self.players[2].credit(5)
    self.players[0].debit(10)
    
    winner = find_winner(self.players)
    self.assertEqual(winner.name, "Aluna")
    
  def test_tie(self):
    """Test when there are multiple players"""
    self.players[1].credit(10)
    self.players[3].debit(16)
    self.players[2].credit(10)
    self.players[0].debit(10)
    
    winners = find_winner(self.players)
    self.assertEqual(winners, "Aluna, Myriam")
    
  def test_all_broke(self):
    """Test when there are multiple players"""
    self.players[0].debit(16)
    self.players[1].debit(16)
    self.players[2].debit(16)
    self.players[3].debit(16)
    
    winners = find_winner(self.players)
    self.assertEqual(winners, None)
    
if __name__ == "__main__":
  unittest.main()