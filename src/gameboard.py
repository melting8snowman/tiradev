import random
#from itertools import cycle
import numpy as np
#import pygame
#from settings import Settings


class Gameboard:
    def __init__(self, settings):
        self.row_count = settings.row_count
        self.column_count = settings.column_count
        self.board = np.zeros((self.row_count, self.column_count))
        self.moves_played = 0
        self.to_win = settings.to_win
        self.max_turns = self.row_count * self.column_count
        self.player = 1
        self.opponent = settings.opponent
        #self.turn = random.randint(self.player, self.opponent)
        self.turn = 1
        self.game_over = False

    def randomize_starter(self):
        self.turn = random.randint(
            self.player, self.opponent)  # Player1 <> Player2/AI

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
        for row in range(self.row_count):
            if self.board[row][col] == 0:
                return row

    def valid_columns(self):
        valid_cols = []
        for column in range(self.column_count):
            if self.is_valid_location(column):
                valid_cols.append(column)
        return valid_cols

    def add_move(self):
        self.moves_played = self.moves_played + 1
        #self.turn += 1
        #self.turn = self.turn % 2
        if self.turn == self.player:
            self.turn = self.opponent
        else:
            self.turn = self.player

    def is_winning_move(self, token):
        # Check horizontal for win
        for col in range(self.column_count-3):
            for row in range(self.row_count):
                if self.board[row][col] == token and self.board[row][col+1] == token and self.board[row][col+2] == token and self.board[row][col+3] == token:
                    self.game_over = True
                    return True
        # Check vertical
        for col in range(self.column_count):
            for row in range(self.row_count-3):
                if self.board[row][col] == token and self.board[row+1][col] == token and self.board[row+2][col] == token and self.board[row+3][col] == token:
                    self.game_over = True
                    return True
            # Check positive diagonal
        for col in range(self.column_count-3):
            for row in range(self.row_count-3):
                if self.board[row][col] == token and self.board[row+1][col+1] == token and self.board[row+2][col+2] == token and self.board[row+3][col+3] == token:
                    self.game_over = True
                    return True
        # Check reverse diagonal
        for col in range(self.column_count-3):
            for row in range(3, self.row_count):
                if self.board[row][col] == token and self.board[row-1][col+1] == token and self.board[row-2][col+2] == token and self.board[row-3][col+3] == token:
                    self.game_over = True
                    return True
        return False

    def draw_board(self, pygame, screen, settings):
        # board
        for col in range(self.column_count):
            for row in range(self.row_count):
                pygame.draw.rect(screen, settings.blue, (col*settings.square_size, row*settings.square_size +
                                 settings.square_size, settings.square_size, settings.square_size))
                pygame.draw.circle(screen, settings.black, (int(col*settings.square_size+settings.square_size/2), int(
                    row*settings.square_size+settings.square_size+settings.square_size/2)), settings.radius)
        # tokens
        for col in range(self.column_count):
            for row in range(self.row_count):
                if self.get_token(row, col) == 1:
                    pygame.draw.circle(screen, settings.red, (int(col*settings.square_size+settings.square_size/2),
                                       settings.height-int(row*settings.square_size+settings.square_size/2)), settings.radius)
                elif self.get_token(row, col) == 2:
                    pygame.draw.circle(screen, settings.white, (int(col*settings.square_size+settings.square_size/2),
                                       settings.height-int(row*settings.square_size+settings.square_size/2)), settings.radius)
                elif self.get_token(row, col) == 3:
                    pygame.draw.circle(screen, settings.yellow, (int(col*settings.square_size+settings.square_size/2),
                                       settings.height-int(row*settings.square_size+settings.square_size/2)), settings.radius)

    def is_final_node(self):
        # return self.is_winning_move(self.board, self.player) or self.is_winning_move(self.board, self.opponent) or self.max_turns - self.moves_played == 0
        return self.is_winning_move(self.player) or self.is_winning_move(self.opponent) or self.max_turns - self.moves_played == 0

    def scoring(self, token):
        # give scores based on token positions.
        # center column(s) most valuable as they count both ways
        # for other positions, most crucial is how many tokens in a row currently
        # these need to be evaluated on board position
        score = 0

        # multiply center column score(s) as columns counting both ways
        # center
        center_pile = [int(i)
                       for i in list(self.board[:, self.column_count//2])]
        center_count = center_pile.count(token)
        score += center_count * max((self.column_count - self.to_win), 1)
        # next to center
        next_to_center_pile = [int(i) for i in list(
            self.board[:, (self.column_count//2+1)])]
        next_to_center_count = next_to_center_pile.count(token)
        score += next_to_center_count * \
            max((self.column_count - self.to_win - 1), 0)

        # score horizontal
        for row in range(self.row_count):
            row_array = [int(i) for i in list(self.board[row, :])]
            for col in range(self.column_count - (self.to_win - 1)):
                zone = row_array[col:col+self.to_win]
                score += self.evaluation(zone, token)

        # score vertical
        for col in range(self.column_count):
            col_array = [int(i) for i in list(self.board[:, col])]
            for row in range(self.row_count - (self.to_win - 1)):
                zone = col_array[row:row+self.to_win]
                score += self.evaluation(zone, token)

        # score diagonal
        for row in range(self.row_count - (self.to_win - 1)):
            for col in range(self.column_count - (self.to_win - 1)):
                zone = [self.board[row+i][col+i] for i in range(self.to_win)]
                score += self.evaluation(zone, token)
        # score reverse diagonal
        for row in range(self.row_count - (self.to_win - 1)):
            for col in range(self.column_count - (self.to_win - 1)):
                zone = [self.board[row + (self.to_win - 1) - i][col+i]
                        for i in range(self.to_win)]
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
        elif zone.count(token) == (self.to_win - 1) and zone.count(empty) == 1:
            score += 7
        elif zone.count(token) == (self.to_win - 2) and zone.count(empty) == 2:
            score += 3
        elif (self.to_win - 3) > 1 and zone.count(token) == (self.to_win - 3) and zone.count(empty) == 3:
            score += 1
            # defence
        elif zone.count(opponent_token) == (self.to_win - 1) and zone.count(empty) == 1:
            score -= 6
        if zone.count(opponent_token) == (self.to_win - 2) and zone.count(empty) == 2:
            score -= 2
        return score
