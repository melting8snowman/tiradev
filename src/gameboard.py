import numpy as np
from settings import Settings 
import pygame

class Gameboard:
    def __init__(self, settings):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.board = np.zeros((self.row_count,self.column_count))        
        self.moves_played = 0
        self.turn = 0
        self.game_over = False

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def print_board(self):
        print(np.flip(self.board, 0))
    
    def get_item(self, row, column):
        return self.board[row][column]

    def is_valid_location(self, col):
        return self.board[self.row_count-1][col] == 0

    def open_row(self, col):
        for r in range(self.row_count):
            if self.board[r][col] == 0:
                return r

    def add_move(self):
        self.moves_played = self.moves_played +1
        self.turn += 1
        self.turn = self.turn % 2
    
    
    def is_winning_move(self, piece):
        # Check horizontal for win
        for c in range(self.column_count-3):
            for r in range(self.row_count):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    self.game_over = True
                    return True

        for c in range(self.column_count):
            for r in range(self.row_count-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    self.game_over = True
                    return True

	    # Check positive diagonal
        for c in range(self.column_count-3):
            for r in range(self.row_count-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    self.game_over = True
                    return True

        # Check negatively diagonal
        for c in range(self.column_count-3):
            for r in range(3, self.row_count):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    self.game_over = True
                    return True
        return False


    def draw_board(self, pygame, screen, settings):
        for c in range(self.column_count):
            for r in range(self.row_count):
                pygame.draw.rect(screen, settings.blue, (c*settings.square_size, r*settings.square_size+settings.square_size, settings.square_size, settings.square_size))
                pygame.draw.circle(screen, settings.black, (int(c*settings.square_size+settings.square_size/2), int(r*settings.square_size+settings.square_size+settings.square_size/2)), settings.radius)
	
        for c in range(self.column_count):
            for r in range(self.row_count):		
                if self.get_item(r,c) == 1:
                    pygame.draw.circle(screen, settings.red, (int(c*settings.square_size+settings.square_size/2), settings.height-int(r*settings.square_size+settings.square_size/2)), settings.radius)
                elif self.get_item(r,c) == 2: 
                    pygame.draw.circle(screen, settings.white, (int(c*settings.square_size+settings.square_size/2), settings.height-int(r*settings.square_size+settings.square_size/2)), settings.radius)
        #pygame.display.update()
  
    
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

