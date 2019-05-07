class Gameboard:
    def __init__(self):
        self.rowLength = 6
        self.columnLength = 7
        self.blankPiece = "_"
        self.board = [[self.blankPiece for x in range(self.columnLength)] for y in range(self.rowLength)]

    def input_piece(self, piece, index):
        try:
            rowColumn = self.get_available_space_in_column(index)
        except:
            print("Column is full. Please choose again.")
        row = rowColumn[0]
        column = rowColumn[1]
        self.board[row][column] = piece
        return rowColumn

    def get_available_space_in_column(self, column):
        for x in range(5, -1, -1):
            if(self.board[x][column] == self.blankPiece):
                return [x,column]
        raise

    def check_winner(self, row, column):
        return self.check_horizontal(row, column) or self.check_vertical(row, column) or self.check_diagonal(row, column)

    def check_diagonal(self, row, column):
        color = self.board[row][column]
        northeast = self.check_northeast(color, row, column)
        northwest = self.check_northwest(color, row, column)
        southeast = self.check_southeast(color, row, column)
        southwest = self.check_southwest(color, row, column)
        return northeast + southwest -1 > 3 or northwest + southeast -1 > 3

    def check_northeast(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_northeast(color, row+1, column+1)
        return 0

    def check_northwest(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_northwest(color, row+1, column-1)
        return 0

    def check_southeast(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_southeast(color, row-1, column+1)
        return 0

    def check_southwest(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_southwest(color, row-1, column-1)
        return 0

    def check_vertical(self, row, column):
        color = self.board[row][column]
        above = self.check_above(color, row, column)
        below = self.check_below(color, row, column)
        return above + below - 1> 3

    def check_below(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_below(color, row+1, column)
        return 0

    def check_above(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_above(color, row-1, column)
        return 0

    def check_horizontal(self, row, column):
        color = self.board[row][column]
        right = self.check_right(color, row, column)
        left = self.check_left(color, row, column)
        return right + left - 1> 3
        
    def check_right(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_right(color, row, column+1)
        return 0

    def check_left(self, color, row, column):
        if(self.is_inside_gameboard_boundaries(row, column) and self.board[row][column] == color):
            return 1 + self.check_left(color, row, column-1)
        return 0

    def is_inside_gameboard_boundaries(self, row, column):
        return not(row >= len(self.board) or column >= len(self.board[row]) or row < 0 or column < 0)

    def printGrid(self):
        for x in range(self.columnLength):
            print(str(x) + "|", end='')
        print('')
        print('')
        for row_count, row in enumerate(self.board):
            for col_count, piece in enumerate(row):
                print(piece + "|", end='')
            print('')
        for x in range(len(row)):
            print('--', end='')
        print('')
