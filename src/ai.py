import math
import random
import copy

#from settings import Settings
from gameboard import Gameboard


class Ai:
    def __init__(self, settings, board):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.to_win = settings.to_win
        self.board = board
        self.opponent = settings.opponent
        #self.moves_played = board.moves_played
        #self.game_over = board.game_over

    def minimax(self, board, depth, alpha, beta, max_player):
        # check for end game
        if board.is_final_node() or depth == 0:
            if board.is_final_node():
                if board.is_winning_move(board.opponent):  # AI
                    # maximize
                    return (None, 999999999)
                elif board.is_winning_move(board.player):  # Player
                    # minimize
                    return (None, -999999999)
                else:  # Game over, no more moves
                    return (None, 0)
            else:  # depth == 0:
                # return (None, self.scoring(board.opponent)) # AI
                return (None, board.scoring(board.opponent))  # AI

        # continue with turn
        valid_cols = board.valid_columns()
        # pick initial "winner" of available columns
        best_column = random.choice(valid_cols)

        if max_player:
            score = -math.inf
            for col in valid_cols:
                # continue game on all valid rows and return best score
                next_row = board.next_open_row(col)
                board_copy = copy.deepcopy(board)
                board_copy.drop_token(next_row, col, board.opponent)
                scenario_score = self.minimax(
                    board_copy, depth-1, alpha, beta, False)[1]
                if scenario_score > score:
                    score = scenario_score
                    best_column = col
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return best_column, score

        else:  # Minimizing player
            score = math.inf
            for col in valid_cols:
                # continue game on all valid rows and return best score
                next_row = board.next_open_row(col)
                board_copy = copy.deepcopy(board)
                board_copy.drop_token(next_row, col, board.player)
                scenario_score = self.minimax(
                    board_copy, depth-1, alpha, beta, True)[1]
                if scenario_score < score:
                    score = scenario_score
                    best_column = col
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return best_column, score
