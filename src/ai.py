from settings import Settings
from gameboard import Gameboard
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
        #self.moves_played = board.moves_played
        #self.game_over = board.game_over


# moved to board to try
    def evaluation2(self, zone, token):
        # evaluate game position based on current focus zone;
        # currently valid rows and empty locations
        score = 0
        empty = 0
        # check whose tokens to look at    
        if token == 1:
            opponent_token = self.opponent
        else:
            opponent_token = 1

        if zone.count(token) == (self.to_win):
            # make sure to win
            score += 9999
            # consequtive own tokens with empty slots remaining in focus zone
        elif zone.count(token) == (self.to_win -1) and zone.count(empty) == 1:
            score += 7
        elif zone.count(token) == (self.to_win -2) and zone.count(empty) == 2:
            score += 3
        elif (self.to_win -3 )>1 and zone.count(token) == (self.to_win -3) and zone.count(empty) == 3:
            score += 1
            # defence
        elif zone.count(opponent_token) == (self.to_win -1) and zone.count(empty) == 1:
            score -= 6
        if zone.count(opponent_token) == (self.to_win -2) and zone.count(empty) == 2:
            score -= 2 
        return score

# moved to board to try
    def scoring2(self, token):
        # give scores based on token positions.
        # center column(s) most valuable as they count both ways
        # for other positions, most crucial is how many tokens in a row currently	
        # these need to be evaluated on board position
        score = 0

        ## multiply center column score(s) as columns counting both ways
        # center
        center_pile = [int(i) for i in list(self.board[:, self.column_count//2])] 
        center_count = center_pile.count(token)
        score += center_count * max((self.col_count - self.to_win),1)
        # next to center
        next_to_center_pile = [int(i) for i in list(self.board[:, (self.column_count//2+1)])]
        next_to_center_count = next_to_center_pile.count(token)    
        score += next_to_center_count * max((self.col_count - self.to_win - 1),0)
    
        # score vertical
        for c in range(self.column_count):
            col_array = [int(i) for i in list(self.board[:,c])]
            for r in range(self.column_count - (self.to_win - 1)):
                zone = col_array[r:r+self.to_win]
                score += self.evaluation(zone, token)

        # score horizontal
        for r in range(self.row_count):
            row_array = [int(i) for i in list(self.board[r,:])]
            for c in range(self.column_count - (self.to_win - 1)):
                zone = row_array[c:c+self.to_win]
                score += self.evaluation(zone, token)
                
        # score diagonal
        for r in range(self.column_count - (self.to_win - 1)):
            for c in range(self.column_count - (self.to_win - 1)):
                zone = [self.board[r+i][c+i] for i in range(self.to_win)]
                score += self.evaluation(zone, token)
        # score reverse diagonal
        for r in range(self.column_count - (self.to_win - 1)):
            for c in range(self.column_count - (self.to_win - 1)):
                zone = [self.board[r+ (self.to_win - 1) - i][c+i] for i in range(self.to_win)]
                score += self.evaluation(zone, token)

        return score
    

    def minimax(self, board, depth, alpha, beta, max_Player):
        # check for end game
        if board.is_final_node() or depth == 0:
            if board.is_final_node():
                if board.is_winning_move(board.opponent): #AI
                    # maximize
                    return (None, 999999999)
                elif board.is_winning_move(board.player): # Player
                    # minimize
                    return (None, -999999999)
                else: # Game over, no more moves
                    return (None, 0)
            else:  # depth == 0:
            #return (None, self.scoring(board.opponent)) # AI
                return (None, board.scoring(board.opponent)) # AI
        
        # continue with turn

        valid_cols = board.valid_columns()
        # pick initial "winner" of available columns
        best_column = random.choice(valid_cols)
        
        if max_Player:
            score = -math.inf
            for col in valid_cols:
                # continue game on all valid rows and return best score
                next_row = board.next_open_row(col)
                board_copy = copy.deepcopy(board)
                board_copy.drop_token(next_row, col, board.opponent)
                scenario_score = self.minimax(board_copy, depth-1, alpha, beta, False)[1]
                if scenario_score > score:
                    score = scenario_score
                    best_column = col
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return best_column, score

        else: # Minimizing player
            score = math.inf
            for col in valid_cols:
                # continue game on all valid rows and return best score
                next_row = board.next_open_row(col)
                board_copy = copy.deepcopy(board)
                board_copy.drop_token(next_row, col, board.player)
                scenario_score = self.minimax(board_copy, depth-1, alpha, beta, True)[1]
                if scenario_score < score:
                    score = scenario_score
                    best_column = col
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return best_column, score
