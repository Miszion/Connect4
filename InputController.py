class InputController:

    @staticmethod
    def getValidColumn(board, player, turnNumber):
        col = int(input("Turn " + str(turnNumber) +": " + player.name + " (" + player.color + "), choose your move: "))

        while ((col > board.columns) or (col <= 0)):
            print("Invalid move, outside board, try again: ")
            col = (int(input("Turn " + str(turnNumber) +": " + player.name + " (" + player.color + "), choose your move: ")))

        while (board.grid[0][col-1] != None):
            print("Invalid move, column " + str(col) + " is full, try again: ")
            col = (int(input("Turn " + str(turnNumber) +": " + player.name + " (" + player.color + "), choose your move: ")))
            while ((col > board.columns) or (col <= 0)):
               print("Invalid move, outside board, try again: ")
               col = (int(input("Turn " + str(turnNumber) +": " + player.name + " (" + player.color + "), choose your move: ")))
        print()
        return col - 1

    @staticmethod
    def getPlayAgain():
        playAgain = input(" Play again? (y/n): ")

        if playAgain == "y":
            return True
        else:
            print("Goodbye!")
            return False

    @staticmethod
    def getGameFilled():
        playAgain = input("Tie Game!  Play again? (y/n): ")
        if playAgain == "y":
            return True
        else:
            print("Goodbye!")
            return False

    @staticmethod
    def promptBoardSize():
        boardSpacing = int(input("Please choose the board spacing: "))
        if (boardSpacing == -1):
            boardSpacing = 0
        return boardSpacing




