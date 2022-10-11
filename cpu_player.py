import player
import gameboard
import random
import utility

class CpuPlayer(player.Player):
    def __init__(self, board, color, name):
        player.Player.__init__(self, color, name)
        self.board = board
        self.name = name
        self.lastRow = -1
        self.lastColumn = -1

    def get_input(self):
        #check if user is about to win
        if self.find_blocking_column():
            return self.lastColumn
        elif self.lastRow >= 0:
            self.find_next_piece_column()
            return self.lastColumn
        else:
            self.set_random_row_and_column()
            return self.lastColumn

    def find_blocking_column(self):
        for row in range(self.board.rowLength-1, -1, -1):
            for column in range(self.board.columnLength):
                if (self.is_location_inbounds(column) 
                     and self.is_player_in_winning_state(self.board.get_vertical_connections_count, row, column)):
                    self.set_last_location(column)
                    return True
                elif (self.is_location_inbounds(column + 3) 
                     and self.is_player_in_winning_state(self.board.get_horizontal_connections_count, row, column)):
                    self.set_last_location(column + 3)
                    return True
                elif (self.is_location_inbounds(column + 3) 
                     and self.is_player_in_winning_state(self.board.get_se_to_nw_connections_count, row, column)):
                    self.set_last_location(column - 3)
                    return True
                elif (self.is_location_inbounds(column + 3) 
                     and self.is_player_in_winning_state(self.board.get_sw_to_ne_connections_count, row, column)):
                    self.set_last_location(column + 3)
                    return True
        return False

    def is_location_inbounds(self, column):
        try:
            self.board.get_available_space_in_column(column)[0]
            return True
        except:
            return False

    def is_player_in_winning_state(self, method, row, column):
        pieceColor = self.board.get_piece(row, column)
        lastPieceInColumn = self.board.get_last_piece_in_column(column)
        if (lastPieceInColumn != self.color
            and (pieceColor != self.color or pieceColor != self.board.blankPiece)):
            return method(row, column) > 2
        return False

    def set_random_row_and_column(self):
        self.set_last_location(self.get_random_column())

    def find_next_piece_column(self):
        if self.lastColumn + 1 < self.board.columnLength and self.board.board[self.lastRow][self.lastColumn+1] == self.board.blankPiece:
            self.set_last_location(self.lastColumn+1)
            
        elif self.lastRow - 1 >= 0 and self.board.board[self.lastRow-1][self.lastColumn] == self.board.blankPiece:
            self.set_last_location(self.lastColumn)

        elif self.lastColumn - 1 >= 0 and self.board.board[self.lastRow][self.lastColumn-1] == self.board.blankPiece:
            self.set_last_location(self.lastColumn-1)

        else:
            self.set_random_row_and_column() 

    def set_last_location(self, column):
        self.lastColumn = column
        self.lastRow = self.board.get_available_space_in_column(self.lastColumn)[0]

    def get_random_column(self):
        return random.randint(0, self.board.columnLength - 1)

    def is_cpu(self):
        return True