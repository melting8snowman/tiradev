import unittest
import pygame
import math
from ai import Ai
from settings import Settings
from gameboard import Gameboard


class TestAi(unittest.TestCase):
    def setUp(self):
        settings = Settings(6, 7, 4, 100, "AI")
        board = Gameboard(settings)
        self.ai = Ai(settings, board)

    def test_created_ai_exists(self):
        self.assertNotEqual(self.ai, None)

    def test_minimax_non_final_node(self):
        self.ai.board.drop_token(1, 1, 1)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, 12)
    
    def test_minimax_minimize(self):
        self.ai.board.drop_token(1, 1, 1)
        self.ai.board.drop_token(2, 1, 3)
        self.ai.board.drop_token(1, 2, 1)
        self.ai.board.drop_token(2, 2, 3)
        self.ai.board.drop_token(1, 3, 1)
        self.ai.board.drop_token(1, 4, 3)
        self.ai.board.drop_token(5, 1, 1)
        self.ai.board.drop_token(2, 4, 3)
        self.ai.board.drop_token(1, 4, 1)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, -999999999)
    
    def test_minimax_maximize(self):
        self.ai.board.drop_token(1, 1, 3)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(1, 2, 3)
        self.ai.board.drop_token(2, 2, 1)
        self.ai.board.drop_token(1, 3, 3)
        self.ai.board.drop_token(3, 2, 1)
        self.ai.board.drop_token(1, 4, 3)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, False)
        self.assertAlmostEqual(minimax_score, 999999999)
    
    def test_minimax_player_won(self):
        self.ai.board.drop_token(1, 1, 1)
        self.ai.board.drop_token(2, 1, 3)
        self.ai.board.drop_token(1, 2, 1)
        self.ai.board.drop_token(2, 2, 3)
        self.ai.board.drop_token(1, 3, 1)
        self.ai.board.drop_token(3, 2, 3)
        self.ai.board.drop_token(1, 4, 1)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, -999999999)

    
    def test_minimax_5(self):
        self.ai.board.drop_token(1, 1, 3)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(1, 2, 3)
        self.ai.board.drop_token(2, 2, 1)
        self.ai.board.drop_token(1, 3, 3)
        self.ai.board.drop_token(3, 2, 1)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, False)
        self.assertAlmostEqual(minimax_score, 5)
        
    def test_minimax_12(self):
        self.ai.board.drop_token(1, 1, 3)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(1, 2, 3)
        self.ai.board.drop_token(2, 2, 1)
        self.ai.board.drop_token(1, 3, 3)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, False)
        self.assertAlmostEqual(minimax_score, 12)
        
    def test_minimax_24(self):
        self.ai.board.drop_token(1, 1, 3)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(1, 2, 3)
        self.ai.board.drop_token(2, 2, 1)
        self.ai.board.drop_token(1, 3, 3)
        self.ai.board.drop_token(3, 2, 1)
        #self.ai.board.drop_token(1, 4, 3)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, 24)
    
    def test_minimax_29(self):
        self.ai.board.drop_token(1, 1, 3)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(1, 2, 3)
        self.ai.board.drop_token(2, 2, 1)
        self.ai.board.drop_token(1, 3, 3)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, 29)
        
    def test_minimax_31(self):
        self.ai.board.drop_token(1, 1, 1)
        self.ai.board.drop_token(2, 1, 3)
        self.ai.board.drop_token(1, 2, 1)
        self.ai.board.drop_token(2, 2, 3)
        self.ai.board.drop_token(1, 3, 1)
        self.ai.board.drop_token(1, 4, 3)
        self.ai.board.drop_token(5, 1, 1)
        self.ai.board.drop_token(2, 4, 3)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, 31)
 
    def test_minimax_full_board(self):        
        self.ai.board.drop_token(0, 2, 3)
        self.ai.board.drop_token(1, 2, 1)
        self.ai.board.drop_token(2, 2, 3)
        self.ai.board.drop_token(3, 2, 1)
        self.ai.board.drop_token(4, 2, 3)
        self.ai.board.drop_token(5, 2, 1)
        
        self.ai.board.drop_token(0, 3, 3)
        self.ai.board.drop_token(1, 3, 1)
        self.ai.board.drop_token(2, 3, 3)
        self.ai.board.drop_token(3, 3, 1)
        self.ai.board.drop_token(4, 3, 3)
        self.ai.board.drop_token(5, 3, 1)
        
        self.ai.board.drop_token(0, 4, 1)
        self.ai.board.drop_token(1, 4, 3)
        self.ai.board.drop_token(2, 4, 1)
        self.ai.board.drop_token(3, 4, 3)
        self.ai.board.drop_token(4, 4, 1)
        self.ai.board.drop_token(5, 4, 3)
        
        self.ai.board.drop_token(0, 5, 1)
        self.ai.board.drop_token(1, 5, 3)
        self.ai.board.drop_token(2, 5, 1)
        self.ai.board.drop_token(3, 5, 3)
        self.ai.board.drop_token(4, 5, 1)

        self.ai.board.drop_token(0, 6, 3)
        self.ai.board.drop_token(1, 6, 1)
        self.ai.board.drop_token(2, 6, 3)
        self.ai.board.drop_token(3, 6, 1)
        self.ai.board.drop_token(4, 6, 3)
        self.ai.board.drop_token(5, 6, 1)
        
        self.ai.board.drop_token(5, 5, 3)
        
        self.ai.board.drop_token(0, 0, 1)
        self.ai.board.drop_token(1, 0, 3)
        self.ai.board.drop_token(2, 0, 1)
        self.ai.board.drop_token(3, 0, 3)
        self.ai.board.drop_token(4, 0, 1)
        self.ai.board.drop_token(5, 0, 3)
        
        self.ai.board.drop_token(0, 1, 1)
        self.ai.board.drop_token(1, 1, 3)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(3, 1, 3)
        self.ai.board.drop_token(4, 1, 1)
        self.ai.board.drop_token(5, 1, 3)

        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, False)
        self.assertAlmostEqual(minimax_score, math.inf) 
    
    def test_minimax_simple(self):
        self.ai.board.drop_token(1, 1, 1)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(3, 1, 1)
        self.ai.board.drop_token(4, 1, 1)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, True)
        self.assertAlmostEqual(minimax_score, -999999999)
    
    def test_minimax_simple2(self):
        self.ai.board.drop_token(1, 1, 1)
        self.ai.board.drop_token(2, 1, 1)
        self.ai.board.drop_token(3, 1, 1)
        self.ai.board.drop_token(4, 1, 1)
        col, minimax_score = self.ai.minimax(self.ai.board, 5, -math.inf, math.inf, False)
        self.assertAlmostEqual(minimax_score, -999999999)


