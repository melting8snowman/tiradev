
class gameboard:
    def __init__(self, gameboard):
        global WHITE
        WHITE = 1
        global RED
        RED = 2
        global COLUMNS
        COLUMNS = 7
        global ROWS
        ROWS = 6
        self.board = []
        for i in range(COLUMNS):
            self.board.append([0] * ROWS)
        global moves_played
        moves_played = 0

    def print_gameboard(self):
        i = 0
        j = 0

        while i < self.ROWS:
            while j < self.COLUMNS:
                print('-' if board[j][i] == 0 else 'X' if board[j][i] == 1 else 'O', end=' ')
                j += 1
            print("")
            i += 1
            j = 0

        print("0 1 2 3 4 5 6")

