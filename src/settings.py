import pygame

class Settings:
    def __init__(self, row_count, column_count, to_win, square_size):
        self.row_count = row_count
        self.column_count = column_count
        self.to_win = to_win
        # set colours
        self.blue = (0,0,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.yellow = (255,255,0)
        # define board UI sizes
        self.square_size = square_size
        self.width = self.column_count * square_size
        self.height = (self.row_count+1) * square_size
        self.size = (self.width, self.height)
        self.radius = int(square_size/2 - 5)

