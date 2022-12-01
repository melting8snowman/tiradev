#import pygame


class Settings:
    def __init__(self, row_count, column_count, to_win, square_size, opponent):
        self.row_count = row_count
        self.column_count = column_count
        self.to_win = to_win
        self.player = 1
        if opponent == "HUMAN":
            self.opponent = 2
        else:
            self.opponent = 3
        # set colours
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.green = (60, 179, 113)
        # define board UI sizes
        self.square_size = square_size
        self.width = self.column_count * square_size
        self.height = (self.row_count+1) * square_size
        self.size = (self.width, self.height)
        self.radius = int(square_size/2 - 5)
