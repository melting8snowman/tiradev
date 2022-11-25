from settings import Settings
from gameboard import Gameboard

class Ai:
    def __init__(self, settings, board):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.board = board        
        self.moves_played = settings.moves_played
        self.game_over = board.game_over

    def evaluation(self, window, piece):
        # evaluate position based on current rows and empty locations
        score = 0
        return score

    def scoring(self, board, settings, piece):
        # give scores based on piece positions.
        # center column(s) most valuable as they count both ways
        # for other positions, most crucial is how many pieces in a row currently	
        # these need to be evaluated on board position
        score = 0

        ## multiply center column score(s) as columns counting both ways
        # center
        center_pile = [int(i) for i in list(board[:, settings.column_count//2])] 
        center_count = center_pile.count(piece)
        score += center_count * max((settings.col_count - settings.to_win),1)
        # next to center
        next_to_center_pile = [int(i) for i in list(board[:, (settings.column_count//2+1)])]
        next_to_center_count = next_to_center_pile.count(piece)    
        score += next_to_center_count * max((settings.col_count - settings.to_win - 1),0)
    
        # score vertical
        for c in range(settings.column_count):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(settings.column_count - (settings.to_win - 1)):
                window = col_array[r:r+settings.to_win]
                score += evaluation(window, piece)

        # score horizontal
        for r in range(settings.row_count):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(settings.column_count - (settings.to_win - 1)):
                window = row_array[c:c+settings.to_win]
                score += evaluation(window, piece)
                
        # score diagonal
        for r in range(settings.column_count - (settings.to_win - 1)):
            for c in range(settings.column_count - (settings.to_win - 1)):
                window = [board[r+i][c+i] for i in range(settings.to_win)]
                score += evaluation(window, piece)
        # score reverse diagponal
        for r in range(settings.column_count - (settings.to_win - 1)):
            for c in range(settings.column_count - (settings.to_win - 1)):
                window = [board[r+ (settings.to_win - 1) - i][c+i] for i in range(settings.to_win)]
                score += evaluation(window, piece)

        return score
