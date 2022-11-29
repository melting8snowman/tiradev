import numpy as np
import sys
import math
import pygame
from gameboard import Gameboard
from settings import Settings


# initiate pygame and font
pygame.init()
pygame.font.init()


# initiate gameboard and setup 
settings = Settings(6,7,4,100)
board = Gameboard(settings)
gamefont = pygame.font.SysFont("monospace", 70)
screen = pygame.display.set_mode(settings.size)
board.draw_board(pygame, screen, settings)
pygame.display.update()


# begin game
while not board.game_over:

    for event in pygame.event.get():
        if board.moves_played == (settings.row_count * settings.column_count):
            label = gamefont.render("Draw!!!!", 1, settings.yellow)
            screen.blit(label, (40,10))
            board.game_over = True
            pygame.display.update()
            pygame.time.wait(5000)
        else:
            token_dropped = False
        
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, settings.black, (0,0, settings.width, settings.square_size))
            position = event.pos[0]
            if board.turn == 0:
                pygame.draw.circle(screen, settings.red, (position, int(settings.square_size/2)), settings.radius)
            else: 
                pygame.draw.circle(screen, settings.white, (position, int(settings.square_size/2)), settings.radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, settings.black, (0,0, settings.width, settings.square_size))
            
            # Player 1
            if board.turn == 0:
                position = event.pos[0]
                col = int(math.floor(position/settings.square_size))
                if board.is_valid_location(col):
                    row = board.next_open_row(col)
                    board.drop_token(row, col, 1)
                    token_dropped = True

                    if board.is_winning_move(1):
                        label = gamefont.render("Player One wins!!!!!", 1, settings.red)
                        screen.blit(label, (40,10))

            #Player 2
            else:				
                position = event.pos[0]
                col = int(math.floor(position/settings.square_size))              
                if board.is_valid_location(col):
                    row = board.next_open_row(col)
                    board.drop_token(row, col, 2)
                    token_dropped = True

                    if board.is_winning_move(2):
                        label = gamefont.render("Player Two wins!!!!", 1, settings.white)
                        screen.blit(label, (40,10))

            #board.print_board()
            board.draw_board(pygame, screen, settings)
            pygame.display.update()
            
            # toggle turn            
            if token_dropped == True:
                board.add_move()
            
            # end game
            if board.game_over:
                pygame.time.wait(5000)