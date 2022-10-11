import sys
import random
import player
import gameboard
import cpu_player

def game_loop():
    isPlaying = parseIsPlaying(input("This is connect four. Would you like to play? Y or N "))
    isSinglePlayer = parseIsPlaying(input("Would like to play against the CPU? Y or N "))
    while(isPlaying):
        board = gameboard.Gameboard()
        player1 = create_player("R", "Player 1")
        player2 = create_player("B", "Player 2") if not(isSinglePlayer) else cpu_player.CpuPlayer(board, "B", "CPU Player 2")
        print(player1.description)
        print(player2.description)
        board.printGrid()
        currentPlayer = player1
        isGameOver = False
        while(not(isGameOver)):
            columnIndex = parseColumnInput(currentPlayer)
            try:
                rowColumn = board.input_piece(currentPlayer.color, columnIndex)
                board.printGrid()
                isGameOver = board.check_winner(rowColumn[0], rowColumn[1])
            except:
                board.printGrid()
                continue
            if(not(isGameOver)):
                currentPlayer = player2 if currentPlayer.color == player1.color else player1

        print(currentPlayer.name + " wins!")
        isPlaying = parseIsPlaying(input("Play again? y or n "))

def parseIsPlaying(isPlayingInput):
    if(isPlayingInput == "N" or isPlayingInput == "n"):
        exit()
    return True

def parseColumnInput(currentPlayer):
    print(currentPlayer.name + "'s turn")
    isParsed = False
    while(not(isParsed)):
        try:
            columnInput = currentPlayer.get_input()
        except:
            print("Input has to be a number from 0 to 6.")
            continue
        if columnInput < 0 or columnInput > 7:
            print("Input has to be one of the columns.")
            continue
        isParsed = True
    return int(columnInput)

def create_player(color, name):
    return player.Player(color, name)

game_loop()