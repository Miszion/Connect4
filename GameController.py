#mission marcus's connect 4 game!
from Game import Game
from InputController import InputController

class GameController:

    def playGame(self, boardSpacing = -1):
        newGame = True
        if (boardSpacing == -1):
            boardSpacing = InputController.promptBoardSize() #ask for the board size.
        else:
            newGame= False

        game1 = Game(6,7,4,boardSpacing) #make a game.

        if (newGame is True):
            game1.view.displayColumnAsk() # display columns
        print("")
        game1.view.display() #display board

        while(game1.isOver is False): #while the game isnt over

            for x in game1.playerList:
                if ((game1.turnNumber == (game1.rows * game1.columns)) & (game1.isOver is not True)):
                    play = InputController.getGameFilled() #the gameboard MUST be filled.
                    if (play):
                        return self.playGame(boardSpacing) #if it is, prompt for restart the game.
                    else:
                        game1.isOver = True #game is over.
                        return
                else:

                    if (game1.isOver is True): #if the game is over..
                         return
                    else:
       
                        game1.turnNumber = game1.turnNumber + 1 #increment turn
                        col = InputController.getValidColumn(game1.view.board, x, game1.turnNumber) #get a valid column
                        if (x.makeMove(game1.view, col) is True): #if this is true
                            game1.isOver = True #game is over.
                            if (InputController.getPlayAgain() is True): #if we play again..
                                return self.playGame(boardSpacing)
                            else:
                                game1.isOver = True #if not, gg
                                return
                       



