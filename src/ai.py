import math
import random
import copy

class Ai:
    def __init__(self, settings, board):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.to_win = settings.to_win
        self.board = board
        self.opponent = settings.opponent

    def minimax(self, board, depth, alpha, beta, max_player):
        # check for end game options
        if board.is_winning_move(board.opponent): 
                    # maximize
            return (None, 999999999)
        if board.is_winning_move(board.player):
                    # minimize
            return (None, -999999999)
        if depth == 0:
            return (None, board.scoring(board.opponent))

        # continue with turn
        valid_cols = board.valid_columns()
        # pick initial "winner" of available columns
        if len(valid_cols) > 0:
            best_column = random.choice(valid_cols)
        else:
            best_column = 0

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
