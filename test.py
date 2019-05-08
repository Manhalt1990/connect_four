import unittest
import gameboard
import cpu_player
import player
import utility

class TestWinningScenarios(unittest.TestCase):

    def testDiagonalWin(self):
        board = gameboard.Gameboard()
        for x in range(4):
            board.board[x][x] = "R"
        self.assertTrue(board.check_diagonal(0,0))

    def testHoriztonalWin(self):
        board = gameboard.Gameboard()
        for x in range(4):
            board.board[0][x] = "R"
        self.assertTrue(board.check_horizontal(0,0))

    def testVerticalWin(self):
        board = gameboard.Gameboard()
        for x in range(4):
            board.board[x][0] = "R"
        self.assertTrue(board.check_vertical(0,0))

class TestGameboard(unittest.TestCase):

    def testIsInsideGame(self):
        board = gameboard.Gameboard()
        board.board[0][0] = "R"
        self.assertTrue(board.has_color_in_location("R", 0, 0))

class TestCpuPlayer(unittest.TestCase):

    def testSetColumnAndRow(self):
        column = 3
        expectedAvailableRow = 4
        board = gameboard.Gameboard()
        cpuPlayer = cpu_player.CpuPlayer(board, "R", "CPU Player")
        board.input_piece(cpuPlayer.color, column)
        actualRow = cpuPlayer.board.get_available_space_in_column(column)[0]
        self.assertTrue(actualRow == expectedAvailableRow)

    def testBlockUserFromHorizontalWin(self):
        expectedColumn = 3
        expectedRow = 5
        board = gameboard.Gameboard()
        cpuPlayer = cpu_player.CpuPlayer(board, "R", "CPU Player")
        player1 = player.Player("R", "Player1")
        board.input_piece(player1.color, 0)
        board.input_piece(player1.color, 1)
        board.input_piece(player1.color, 2)
        actualColumn = cpuPlayer.get_input()
        actualRow = cpuPlayer.lastRow
        board.input_piece(cpuPlayer.color, actualColumn)
        self.assertTrue(actualColumn == expectedColumn and actualRow == expectedRow and board.get_piece(actualRow, actualColumn) == cpuPlayer.color)

    def testBlockUserFromVerticalWin(self):
        expectedColumn = 0
        expectedRow = 2
        board = gameboard.Gameboard()
        cpuPlayer = cpu_player.CpuPlayer(board, "B", "CPU Player")
        player1 = player.Player("R", "Player1")
        board.input_piece(player1.color, 0)
        board.input_piece(player1.color, 0)
        board.input_piece(player1.color, 0)
        actualColumn = cpuPlayer.get_input()
        actualRow = cpuPlayer.lastRow
        board.input_piece(cpuPlayer.color, actualColumn)
        self.assertTrue(actualColumn == expectedColumn and actualRow == expectedRow and board.get_piece(actualRow, actualColumn) == cpuPlayer.color)

    def testBlockUserFromSWToNEWin(self):
        expectedColumn = 3
        expectedRow = 2
        board = gameboard.Gameboard()
        cpuPlayer = cpu_player.CpuPlayer(board, "B", "CPU Player")
        player1 = player.Player("R", "Player1")

        board.input_piece(player1.color, 0)
        board.input_piece(cpuPlayer.color, 1)
        board.input_piece(player1.color, 1)
        board.input_piece(cpuPlayer.color, 2)
        board.input_piece(player1.color, 2)
        board.input_piece(player1.color, 2)
        board.input_piece(cpuPlayer.color, 3)
        board.input_piece(player1.color, 3)
        board.input_piece(player1.color, 3)

        actualColumn = cpuPlayer.get_input()
        actualRow = cpuPlayer.lastRow
        board.input_piece(cpuPlayer.color, actualColumn)
        self.assertTrue(actualColumn == expectedColumn and actualRow == expectedRow and board.get_piece(actualRow, actualColumn) == cpuPlayer.color)

    def testBlockUserFromNWToSEWin(self):
        expectedColumn = 0
        expectedRow = 2
        board = gameboard.Gameboard()
        cpuPlayer = cpu_player.CpuPlayer(board, "B", "CPU Player")
        player1 = player.Player("R", "Player1")

        board.input_piece(player1.color, 0)
        board.input_piece(cpuPlayer.color, 0)
        board.input_piece(player1.color, 0)
        board.input_piece(cpuPlayer.color, 1)
        board.input_piece(player1.color, 1)
        board.input_piece(player1.color, 1)
        board.input_piece(cpuPlayer.color, 2)
        board.input_piece(player1.color, 2)
        board.input_piece(player1.color, 3)

        actualColumn = cpuPlayer.get_input()
        actualRow = cpuPlayer.lastRow
        board.input_piece(cpuPlayer.color, actualColumn)
        self.assertTrue(actualColumn == expectedColumn and actualRow == expectedRow and board.get_piece(actualRow, actualColumn) == cpuPlayer.color)

if __name__ == '__main__':
    unittest.main()