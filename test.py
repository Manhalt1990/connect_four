import unittest
import gameboard
import cpu_player

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
        availableRow = cpuPlayer.board.get_available_space_in_column(column)[0]
        self.assertTrue(availableRow == expectedAvailableRow)

if __name__ == '__main__':
    unittest.main()