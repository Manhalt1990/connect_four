import pytest
import unittest
from src import gameboard

class TestGameboard(unittest.TestCase):

    def test_input_piece(self):
        board = gameboard.Gameboard()
        piece = "B"
        index = 0
        rowColumn = board.input_piece(piece, index)
        expectedRowColumn = [5,0]
        self.assertEqual(expectedRowColumn, rowColumn)

    def test_input_piece_column_full(self):
        board = gameboard.Gameboard()
        piece = "B"
        index = 0
        for i in range(0,6):
            board.board[i][0] = piece
        board.printGrid()
        with pytest.raises(UnboundLocalError):
            board.input_piece(piece, index)

    def test_get_available_space_in_column(self):
        board = gameboard.Gameboard()
        expected_rowColumn = [5,0]
        actual_rowColumn = board.get_available_space_in_column(0)
        self.assertEqual(expected_rowColumn, actual_rowColumn)

    def test_get_available_space_in_column_outofbounds(self):
        board = gameboard.Gameboard()
        for i in range(0,6):
            board.board[i][0] = "B"
        with pytest.raises(RuntimeError):
            board.get_available_space_in_column(0)

    def test_get_last_piece_in_column(self):
        board = gameboard.Gameboard()
        piece = "B"
        index = 0
        board.input_piece(piece, index)
        actual_piece = board.get_last_piece_in_column(index)
        expected_piece = piece
        self.assertEqual(expected_piece, actual_piece)

    def test_get_last_piece_in_column_blank_column(self):
        board = gameboard.Gameboard()
        index = 0
        actual_piece = board.get_last_piece_in_column(index)
        expected_piece = board.blankPiece
        self.assertEqual(expected_piece, actual_piece)

    # def test_get_last_piece_in_column_toolarge(self):
    #     board = gameboard.Gameboard()
    #     piece = "B"
    #     index = 0
    #     board.input_piece(piece, index)
    #     actual_piece = board.get_last_piece_in_column(7)
    #     expected_piece = piece
    #     self.assertEqual(expected_piece, actual_piece)

    def test_check_winner(self):
        board = gameboard.Gameboard()
        row = 5
        column = 0
        # Check vertical win
        for i in range(0,4):
            board.board[i][0] = "B"
        self.assertTrue(board.check_winner(row, column))

        #Check horizontal win
        board = gameboard.Gameboard()
        for i in range(0,4):
            board.board[5][i] = "B"
        self.assertTrue(board.check_winner(row, column))

        #Check diagonal win
        board = gameboard.Gameboard()
        for i in range(0,4):
            board.board[5-i][i] = "B"
        self.assertTrue(board.check_winner(row, column))

        #Check non winner
        board = gameboard.Gameboard()
        for i in range(0,3):
            board.board[5-i][i] = "B"
        self.assertFalse(board.check_winner(row, column))

    def test_check_diagonal(self):
        board = gameboard.Gameboard()
        row = 5
        column = 0
        for i in range(0,4):
            board.board[5-i][i] = "B"
        self.assertTrue(board.check_diagonal(row, column))

        #Check non winner
        board = gameboard.Gameboard()
        for i in range(0,3):
            board.board[5-i][i] = "B"
        self.assertFalse(board.check_winner(row, column))

    def test_get_se_to_nw_connections_count(self):
        board = gameboard.Gameboard()
        row = 5
        column = 0
        for i in range(0,4):
            board.board[5-i][i] = "B"
        self.assertEqual(1, board.get_se_to_nw_connections_count(row, column))

        board = gameboard.Gameboard()
        row = 5
        column = 6
        for i in range(0, 4):
            board.board[5-i][6-i] = "B"
        self.assertEqual(4, board.get_se_to_nw_connections_count(row, column))

    def test_is_row_inside_bounds(self):
        board = gameboard.Gameboard()
        self.assertTrue(board.is_row_inside_bounds(2))
        self.assertFalse(board.is_row_inside_bounds(9))

    def test_is_column_inside_bounds(self):
        board = gameboard.Gameboard()
        self.assertTrue(board.is_row_inside_bounds(2))
        self.assertFalse(board.is_row_inside_bounds(9))