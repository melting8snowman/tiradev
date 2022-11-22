import unittest
from gameboard import Gameboard

class TestGameboard(unittest.TestCase):
    def setUp(self):
        self.gameboard = Gameboard()

    def test_created_gameboard_exists(self):
        self.assertNotEqual(self.gameboard, None)
    
    def test_get_item_returns_piece(self):
        self.gameboard.drop_piece(1, 1, 1)
        self.assertAlmostEqual(self.gameboard.get_item(1,1), 1)
    
    def test_drop_piece_puts_piece(self):
        self.gameboard.drop_piece(2, 2, 2)
        self.assertEqual(self.gameboard.get_item(2,2), 2)
    
    def test_is_valid_location(self):
        self.assertEqual(self.gameboard.is_valid_location(3), True)
    def test_is_valid_location2(self):
        self.gameboard.drop_piece(1, 1, 1)
        self.gameboard.drop_piece(2, 1, 2)
        self.gameboard.drop_piece(3, 1, 1)
        self.gameboard.drop_piece(4, 1, 2)
        self.gameboard.drop_piece(5, 1, 1)
        self.assertEqual(self.gameboard.is_valid_location(1), False)
    def test_winning_move(self):
        self.gameboard.drop_piece(1, 1, 1)
        self.gameboard.drop_piece(2, 1, 2)
        self.gameboard.drop_piece(1, 2, 1)
        self.gameboard.drop_piece(2, 2, 2)
        self.gameboard.drop_piece(1, 3, 1)
        self.gameboard.drop_piece(5, 1, 1)
        self.gameboard.drop_piece(1, 4, 1)
        self.assertEqual(self.gameboard.is_winning_move(1), True)
