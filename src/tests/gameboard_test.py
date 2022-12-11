import unittest
import pygame
from gameboard import Gameboard
from settings import Settings


class TestGameboard(unittest.TestCase):
    def setUp(self):
        settings = Settings(6, 7, 4, 100, "HUMAN")
        self.gameboard = Gameboard(settings)


    def test_created_gameboard_exists(self):
        self.assertNotEqual(self.gameboard, None)

    def test_get_token_returns_token(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertAlmostEqual(self.gameboard.get_token(1, 1), 1)

    def test_drop_token_puts_token(self):
        self.gameboard.drop_token(2, 2, 2)
        self.assertEqual(self.gameboard.get_token(2, 2), 2)

    def test_add_move(self):
        self.gameboard.add_move()
        self.assertEqual(self.gameboard.moves_played, 1)
        
    def test_add_move2(self):
        self.gameboard.add_move()
        self.gameboard.add_move()
        self.assertEqual(self.gameboard.moves_played, 2)

    def test_next_open_row_0(self):
        self.assertEqual(self.gameboard.next_open_row(1), 0)
    
    def test_randomize_starter(self):
        self.gameboard.randomize_starter()
        self.assertNotEqual(self.gameboard.turn, 0)

    def test_open_row_none(self):
        self.gameboard.drop_token(0, 1, 1)
        self.gameboard.drop_token(1, 1, 2)
        self.gameboard.drop_token(2, 1, 1)
        self.gameboard.drop_token(3, 1, 2)
        self.gameboard.drop_token(4, 1, 1)
        self.gameboard.drop_token(5, 1, 2)
        self.assertEqual(self.gameboard.next_open_row(1), None)
    
    def test_valid_columns_all(self):
        self.gameboard.drop_token(0, 1, 1)
        self.assertEqual(self.gameboard.valid_columns(), [0, 1, 2, 3, 4, 5, 6])
        
    def test_valid_columns_1_5(self):
        self.gameboard.drop_token(0, 1, 1)
        self.gameboard.drop_token(1, 1, 2)
        self.gameboard.drop_token(2, 1, 1)
        self.gameboard.drop_token(3, 1, 2)
        self.gameboard.drop_token(4, 1, 1)
        self.gameboard.drop_token(5, 1, 2)
        self.assertEqual(self.gameboard.valid_columns(), [0, 2, 3, 4, 5, 6])

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
    
    def test_scoring(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.scoring(1), 0)
    
    def test_scoring_2(self):
        self.gameboard.drop_token(1, 4, 1)
        self.gameboard.drop_token(2, 0, 2)
        self.gameboard.drop_token(2, 3, 1)
        self.gameboard.drop_token(2, 5, 2)
        self.gameboard.drop_token(3, 2, 1)
        self.gameboard.drop_token(3, 5, 2)
        self.gameboard.drop_token(4, 1, 1)
        self.assertGreater(self.gameboard.scoring(1), 1000)

    def test_evaluation_1_0(self):
        zone = [2,0,0,1]
        self.assertEqual(self.gameboard.evaluation(zone, 1), 0)
        
    def test_evaluation_3_0(self):
        zone = [2,0,0,1]
        self.assertEqual(self.gameboard.evaluation(zone, 2), 0)
    
    def test_evaluation_3_3(self):
        zone = [2,2,0,0]
        self.assertEqual(self.gameboard.evaluation(zone, 2), 3)
    
    def test_evaluation_3__3(self):
        zone = [2,0,2,0]
        self.assertEqual(self.gameboard.evaluation(zone, 2), 3)
    
    def test_evaluation_3__7(self):
        zone = [0,2,2,2]
        self.assertEqual(self.gameboard.evaluation(zone, 2), 7)
    
    def test_evaluation_3_7(self):
        zone = [2,2,2,0]
        self.assertEqual(self.gameboard.evaluation(zone, 2), 7)
    
    def test_evaluation_3_9999(self):
        zone = [2,2,2,2]
        self.assertEqual(self.gameboard.evaluation(zone, 2), 9999)
        
    def test_evaluation_1__0(self):
        zone = [2,2,2,2]
        self.assertEqual(self.gameboard.evaluation(zone, 1), 0)
    
    def test_evaluation_defence(self):   
        zone = [2,2,2,0]
        self.assertEqual(self.gameboard.evaluation(zone, 1), -6) 

    def test_evaluation_large_3_3(self):   
        zone = [3,3,0,3,0]
        settings_large = Settings(6, 8, 5, 100, "AI")
        gameboard_large = Gameboard(settings_large)
        self.assertEqual(gameboard_large.evaluation(zone, 3), 3) 
        
    def test_evaluation_large_3_1(self):   
        zone = [3,0,0,3,0]
        settings_large = Settings(6, 8, 5, 100, "AI")
        gameboard_large = Gameboard(settings_large)
        self.assertEqual(gameboard_large.evaluation(zone, 3), 1) 
        
    def test_is_final_node(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.is_final_node(), False)

    def test_print_board(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.print_board(), None)
    
    def test_remove_token(self):
        self.gameboard.drop_token(1, 1, 1)
        self.gameboard.remove_token(1, 1)
        self.assertEqual(self.gameboard.get_token(1, 1), 0)

    def test_print_gameboard(self):
        self.gameboard.drop_token(1, 1, 1)
        self.assertEqual(self.gameboard.print_board(), None)
