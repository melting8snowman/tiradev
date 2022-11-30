import unittest
import pygame
from gameboard import Gameboard
from settings import Settings

class TestGameboard(unittest.TestCase):
    def setUp(self):
        settings = Settings(6,7,4,100, "HUMAN")
        self.gameboard = Gameboard(settings)

    def test_created_gameboard_exists(self):
        self.assertNotEqual(self.gameboard, None)
    
    def test_get_token_returns_token(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertAlmostEqual(self.gameboard.get_token(1,1), 1)
    
    def test_drop_token_puts_token(self):
        self.gameboard.drop_token(2, 2, 2)
        self.assertEqual(self.gameboard.get_token(2,2), 2)
        
    def test_add_move(self):
        self.gameboard.add_move()
        self.assertEqual(self.gameboard.moves_played, 1)

    def test_next_open_row_0(self):
        self.assertEqual(self.gameboard.next_open_row(1), 0)
        
    def test_open_row_none(self):
        self.gameboard.drop_token(0, 1, 1)
        self.gameboard.drop_token(1, 1, 2)
        self.gameboard.drop_token(2, 1, 1)
        self.gameboard.drop_token(3, 1, 2)
        self.gameboard.drop_token(4, 1, 1)
        self.gameboard.drop_token(5, 1, 2)
        self.assertEqual(self.gameboard.next_open_row(1), None)
    
    def test_is_valid_location(self):
        self.assertEqual(self.gameboard.is_valid_location(3), True)
    def test_is_valid_location_false(self):
        self.gameboard.drop_token(1, 1, 1)
        self.gameboard.drop_token(2, 1, 2)
        self.gameboard.drop_token(3, 1, 1)
        self.gameboard.drop_token(4, 1, 2)
        self.gameboard.drop_token(5, 1, 1)
        self.assertEqual(self.gameboard.is_valid_location(1), False)
    def test_winning_move_col(self):
        self.gameboard.drop_token(1, 1, 1)
        self.gameboard.drop_token(2, 1, 2)
        self.gameboard.drop_token(1, 2, 1)
        self.gameboard.drop_token(2, 2, 2)
        self.gameboard.drop_token(1, 3, 1)
        self.gameboard.drop_token(5, 1, 1)
        self.gameboard.drop_token(1, 4, 1)
        self.assertEqual(self.gameboard.is_winning_move(1), True)
    def test_winning_move_row(self):
        self.gameboard.drop_token(1, 1, 1)
        self.gameboard.drop_token(1, 5, 2)
        self.gameboard.drop_token(2, 1, 1)
        self.gameboard.drop_token(2, 5, 2)
        self.gameboard.drop_token(3, 1, 1)
        self.gameboard.drop_token(3, 5, 2)
        self.gameboard.drop_token(4, 1, 1)
        self.assertEqual(self.gameboard.is_winning_move(1), True)
    def test_winning_move_diag(self):
        self.gameboard.drop_token(1, 1, 1)
        self.gameboard.drop_token(2, 0, 2)
        self.gameboard.drop_token(2, 2, 1)
        self.gameboard.drop_token(2, 5, 2)
        self.gameboard.drop_token(3, 3, 1)
        self.gameboard.drop_token(3, 5, 2)
        self.gameboard.drop_token(4, 4, 1)
        self.assertEqual(self.gameboard.is_winning_move(1), True)
    def test_winning_move_rev_diag(self):
        self.gameboard.drop_token(1, 4, 1)
        self.gameboard.drop_token(2, 0, 2)
        self.gameboard.drop_token(2, 3, 1)
        self.gameboard.drop_token(2, 5, 2)
        self.gameboard.drop_token(3, 2, 1)
        self.gameboard.drop_token(3, 5, 2)
        self.gameboard.drop_token(4, 1, 1)
        self.assertEqual(self.gameboard.is_winning_move(1), True)
    
    def test_winning_move_False(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.is_winning_move(1), False)
    
    def test_print_board(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.print_board(), None)
    def test_print_gameboard(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.print_board(), None)
