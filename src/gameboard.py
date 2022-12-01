import numpy as np
import pygame
import random
from itertools import cycle
from settings import Settings 



class Gameboard:
    def __init__(self, settings):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.board = np.zeros((self.row_count,self.column_count))        
        self.moves_played = 0
        self.to_win = settings.to_win
        self.max_turns = self.row_count * self.column_count   
        self.player = 1
        self.opponent = settings.opponent
        #self.turn = random.randint(self.player, self.opponent)
        self.turn = 1
        self.game_over = False

    def randomize_starter(self):
        self.turn = random.randint(self.player, self.opponent) # Player1 <> Player2/AI       

    def drop_token(self, row, col, token):
        self.board[row][col] = token
        
    def remove_token(self, row, col):
        self.board[row][col] = 0

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

    def valid_columns(self):
        valid_cols = []
        for column in range(self.column_count):
            if self.is_valid_location(column):
                valid_cols.append(column)
        return valid_cols

    def add_move(self):
        self.moves_played = self.moves_played +1
        #self.turn += 1
        #self.turn = self.turn % 2
        if self.turn == self.player:
            self.turn = self.opponent
        else:
            self.turn = self.player

    
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
                elif self.get_token(r,c) == 3: 
                    pygame.draw.circle(screen, settings.yellow, (int(c*settings.square_size+settings.square_size/2), settings.height-int(r*settings.square_size+settings.square_size/2)), settings.radius)

    def is_final_node(self):
        #return self.is_winning_move(self.board, self.player) or self.is_winning_move(self.board, self.opponent) or self.max_turns - self.moves_played == 0
        return self.is_winning_move(self.player) or self.is_winning_move(self.opponent) or self.max_turns - self.moves_played == 0

    def scoring(self, token):
        # give scores based on token positions.
        # center column(s) most valuable as they count both ways
        # for other positions, most crucial is how many tokens in a row currently	
        # these need to be evaluated on board position
        score = 0

        ## multiply center column score(s) as columns counting both ways
        # center
        center_pile = [int(i) for i in list(self.board[:, self.column_count//2])] 
        center_count = center_pile.count(token)
        score += center_count * max((self.column_count - self.to_win),1)
        # next to center
        next_to_center_pile = [int(i) for i in list(self.board[:, (self.column_count//2+1)])]
        next_to_center_count = next_to_center_pile.count(token)    
        score += next_to_center_count * max((self.column_count - self.to_win - 1),0)
    
        # score horizontal
        for r in range(self.row_count):
            row_array = [int(i) for i in list(self.board[r,:])]
            for c in range(self.column_count - (self.to_win - 1)):
                zone = row_array[c:c+self.to_win]
                score += self.evaluation(zone, token)
    
        # score vertical
        for c in range(self.column_count):
            col_array = [int(i) for i in list(self.board[:,c])]
            for r in range(self.row_count - (self.to_win - 1)):
                zone = col_array[r:r+self.to_win]
                score += self.evaluation(zone, token)


                
        # score diagonal
        for r in range(self.row_count - (self.to_win - 1)):
            for c in range(self.column_count - (self.to_win - 1)):
                zone = [self.board[r+i][c+i] for i in range(self.to_win)]
                score += self.evaluation(zone, token)
        # score reverse diagonal
        for r in range(self.row_count - (self.to_win - 1)):
            for c in range(self.column_count - (self.to_win - 1)):
                zone = [self.board[r+ (self.to_win - 1) - i][c+i] for i in range(self.to_win)]
                score += self.evaluation(zone, token)

        return score
    
    
    def evaluation(self, zone, token):
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