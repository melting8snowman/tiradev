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

    def drop_token(self, row, col, token):
        self.board[row][col] = token

    def print_board(self):
        print(np.flip(self.board, 0))
    
    def get_token(self, row, column):
        return self.board[row][column]

    def is_valid_location(self, col):
        return self.board[self.row_count-1][col] == 0

    def next_open_row(self, col):
        for r in range(self.row_count):
            if self.board[r][col] == 0:
                return r

    def get_valid_columns(self):
        valid_columns = []
        for column in range(self.column_count):
            if self.is_valid_location(self.board, column):
                valid_columns.append(column)
        return valid_columns

    def add_move(self):
        self.moves_played = self.moves_played +1
        self.turn += 1
        self.turn = self.turn % 2
    
    def is_winning_move(self, token):
        # Check horizontal for win
        for c in range(self.column_count-3):
            for r in range(self.row_count):
                if self.board[r][c] == token and self.board[r][c+1] == token and self.board[r][c+2] == token and self.board[r][c+3] == token:
                    self.game_over = True
                    return True
        # Check vertical
        for c in range(self.column_count):
            for r in range(self.row_count-3):
                if self.board[r][c] == token and self.board[r+1][c] == token and self.board[r+2][c] == token and self.board[r+3][c] == token:
                    self.game_over = True
                    return True
	    # Check positive diagonal
        for c in range(self.column_count-3):
            for r in range(self.row_count-3):
                if self.board[r][c] == token and self.board[r+1][c+1] == token and self.board[r+2][c+2] == token and self.board[r+3][c+3] == token:
                    self.game_over = True
                    return True
        # Check reverse diagonal
        for c in range(self.column_count-3):
            for r in range(3, self.row_count):
                if self.board[r][c] == token and self.board[r-1][c+1] == token and self.board[r-2][c+2] == token and self.board[r-3][c+3] == token:
                    self.game_over = True
                    return True
        return False

    def draw_board(self, pygame, screen, settings):
        # board
        for c in range(self.column_count):
            for r in range(self.row_count):
                pygame.draw.rect(screen, settings.blue, (c*settings.square_size, r*settings.square_size+settings.square_size, settings.square_size, settings.square_size))
                pygame.draw.circle(screen, settings.black, (int(c*settings.square_size+settings.square_size/2), int(r*settings.square_size+settings.square_size+settings.square_size/2)), settings.radius)
        # tokens
        for c in range(self.column_count):
            for r in range(self.row_count):		
                if self.get_token(r,c) == 1:
                    pygame.draw.circle(screen, settings.red, (int(c*settings.square_size+settings.square_size/2), settings.height-int(r*settings.square_size+settings.square_size/2)), settings.radius)
                elif self.get_token(r,c) == 2: 
                    pygame.draw.circle(screen, settings.white, (int(c*settings.square_size+settings.square_size/2), settings.height-int(r*settings.square_size+settings.square_size/2)), settings.radius)

