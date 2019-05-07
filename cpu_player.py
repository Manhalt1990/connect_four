import player
import gameboard
import random

class CpuPlayer(player.Player):
    def __init__(self, board, color, name):
        player.Player.__init__(self, color, name)
        self.board = board
        self.name = name
        self.lastRow = -1
        self.lastColumn = -1

    def get_input(self):
        if self.lastRow >= 0:
            self.find_next_piece_column()
            return self.lastColumn
        else:
            self.set_random_row_and_column()
            return self.lastColumn

    def set_random_row_and_column(self):
        self.lastColumn = self.get_random_column()
        self.lastRow = self.board.get_available_space_in_column(self.lastColumn)[0]

    def find_next_piece_column(self):
        if self.lastColumn + 1 < self.board.columnLength and self.board.board[self.lastRow][self.lastColumn+1] == self.board.blankPiece:
            self.lastColumn = self.lastColumn+1
            self.lastRow = self.board.get_available_space_in_column(self.lastColumn)[0]
        elif self.lastRow - 1 >= 0 and self.board.board[self.lastRow-1][self.lastColumn] == self.board.blankPiece:
            self.lastRow = self.board.get_available_space_in_column(self.lastColumn)[0]
        elif self.lastColumn - 1 >= 0 and self.board.board[self.lastRow][self.lastColumn-1] == self.board.blankPiece:
            self.lastColumn = self.lastColumn-1
            self.lastRow = self.board.get_available_space_in_column(self.lastColumn)[0]
        else:
            self.set_random_row_and_column()

    
    def get_random_column(self):
        return random.randint(0, self.board.columnLength - 1)

    def is_cpu(self):
        return True