import numpy as np
import sys
import math
import pygame
from gameboard import Gameboard


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)




def draw_board(board):
    for c in range(board.COLUMN_COUNT):
        for r in range(board.ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
    for c in range(board.COLUMN_COUNT):
        for r in range(board.ROW_COUNT):		
            if board.get_item(r,c) == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board.get_item(r,c) == 2: 
                pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

#begin
board = Gameboard()
board.print_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
width = board.COLUMN_COUNT * SQUARESIZE
height = (board.ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
myfont = pygame.font.SysFont("monospace", 70)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            position = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (position, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, WHITE, (position, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))

            if turn == 0:
                position = event.pos[0]
                col = int(math.floor(position/SQUARESIZE))

                if board.is_valid_location(col):
                    row = board.open_row(col)
                    board.drop_piece(row, col, 1)

                    if board.is_winning_move(1):
                        label = myfont.render("Player One wins!!!!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True


            #Player 2
            else:				
                position = event.pos[0]
                col = int(math.floor(position/SQUARESIZE))

                if board.is_valid_location(col):
                    row = board.open_row(col)
                    board.drop_piece(row, col, 2)

                    if board.is_winning_move(2):
                        label = myfont.render("Player Two wins!!!!", 1, WHITE)
                        screen.blit(label, (40,10))
                        game_over = True

            board.print_board()
            board.add_move()
            draw_board(board)
            pygame.display.update()

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(5000)