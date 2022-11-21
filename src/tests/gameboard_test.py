import unittest
from gameboard import gameboard

class Testgameboard(unittest.TestCase):
    def setUp(self):
        self.gameboard = gameboard()

    def test_created_gameboard_exists(self):
        self.assertNotEqual(self.gameboard, None)
    
    def get_item_returns_piece(self):
        self.drop_piece(1, 1, 1)
        self.assertEqual(self.get_item(1,1), "1")
    
    def drop_piece_puts_piece(self):
        self.drop_piece(1, 1, 1)
        self.assertEqual(self.gameboard[1][1], 1)