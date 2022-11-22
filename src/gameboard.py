import numpy as np

class Gameboard:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = np.zeros((self.ROW_COUNT,self.COLUMN_COUNT))        
        self.moves_played = 0

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def print_board(self):
        print(np.flip(self.board, 0))
    
    def get_item(self, row, column):
        return self.board[row][column]

    def is_valid_location(self, col):
        return self.board[self.ROW_COUNT-1][col] == 0

    def open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def add_move(self):
        self.moves_played = self.moves_played +1
    
    
    def is_winning_move(self, piece):
        # Check horizontal for win
        for c in range(self.COLUMN_COUNT-3):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

	    # Check positive diagonal
        for c in range(self.COLUMN_COUNT-3):
            for r in range(self.ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negatively diagonal
        for c in range(self.COLUMN_COUNT-3):
            for r in range(3, self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False
    
    
    def print_gameboard(self):
        i = 0
        j = 0

        while i < self.ROWS:
            while j < self.COLUMNS:
                print('-' if self.board[j][i] == 0 else 'X' if self.board[j][i] == 1 else 'O', end=' ')
                j += 1
            print("")
            i += 1
            j = 0

        print("0 1 2 3 4 5 6")

