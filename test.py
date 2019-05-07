import unittest
import gameboard

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

if __name__ == '__main__':
    unittest.main()