from settings import Settings
from gameboard import Gameboard

class Ai:
    def __init__(self, settings, board):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.to_win = settings.to_win
        self.board = board        
        self.moves_played = settings.moves_played
        self.game_over = board.game_over

    def evaluation(self, zone, token):
        # evaluate game position based on current focus zone;
        # currently valid rows and empty locations
        score = 0
        # check whose tokens to look at    
        if token == 1:
            opp_token = 2
        else:
            opp_token = 1

        if zone.count(token) == (self.to_win):
            # make sure to win
            score += 9999
            # consequtive own tokens with empty slots remaining in focus zone
        elif zone.count(token) == (self.to_win -1) and zone.count(EMPTY) == 1:
            score += 7
        elif zone.count(token) == (self.to_win -2) and zone.count(EMPTY) == 2:
            score += 3
        elif (self.to_win -3 )>1 and zone.count(token) == (self.to_win -3) and zone.count(EMPTY) == 3:
            score += 1
            # defence
        elif zone.count(opp_token) == (self.to_win -1) and zone.count(EMPTY) == 1:
            score -= 6
        if zone.count(opp_token) == (self.to_win -2) and zone.count(EMPTY) == 2:
            score -= 2 
        return score

    def scoring(self, board, settings, token):
        # give scores based on token positions.
        # center column(s) most valuable as they count both ways
        # for other positions, most crucial is how many tokens in a row currently	
        # these need to be evaluated on board position
        score = 0

        ## multiply center column score(s) as columns counting both ways
        # center
        center_pile = [int(i) for i in list(board[:, settings.column_count//2])] 
        center_count = center_pile.count(token)
        score += center_count * max((settings.col_count - settings.to_win),1)
        # next to center
        next_to_center_pile = [int(i) for i in list(board[:, (settings.column_count//2+1)])]
        next_to_center_count = next_to_center_pile.count(token)    
        score += next_to_center_count * max((settings.col_count - settings.to_win - 1),0)
    
        # score vertical
        for c in range(settings.column_count):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(settings.column_count - (settings.to_win - 1)):
                zone = col_array[r:r+settings.to_win]
                score += self.evaluation(zone, token)

        # score horizontal
        for r in range(settings.row_count):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(settings.column_count - (settings.to_win - 1)):
                zone = row_array[c:c+settings.to_win]
                score += self.evaluation(zone, token)
                
        # score diagonal
        for r in range(settings.column_count - (settings.to_win - 1)):
            for c in range(settings.column_count - (settings.to_win - 1)):
                zone = [board[r+i][c+i] for i in range(settings.to_win)]
                score += self.evaluation(zone, token)
        # score reverse diagonal
        for r in range(settings.column_count - (settings.to_win - 1)):
            for c in range(settings.column_count - (settings.to_win - 1)):
                zone = [board[r+ (settings.to_win - 1) - i][c+i] for i in range(settings.to_win)]
                score += self.evaluation(zone, token)

        return score
