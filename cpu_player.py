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

        column = self.get_random_column() if self.lastRow < 0 else self.get_next_column(self.lastRow, self.lastColumn)
        try:
            location = self.board.get_available_space_in_column(column)
        except:
            location = [self.get_random_row(), self.get_random_column()]
        self.lastRow = location[0]
        self.lastColumn = location[1]
        return self.lastColumn

    def get_random_row(self):
        return random.randint(0, self.board.rowLength - 1)

    def get_random_column(self):
        return random.randint(0, self.board.columnLength - 1)

    def get_next_column(self, row, column):
        right = self.board.check_right(self.color, row, column)
        left = self.board.check_left(self.color, row, column)
        above = self.board.check_above(self.color, row, column)
        below = self.board.check_below(self.color, row, column)

        if right + left > above + left:
            return column + 1 if column + 1 < self.board.columnLength else column - 1
        else:
            return column

    def is_cpu(self):
        return True