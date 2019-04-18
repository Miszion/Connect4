#Mission Marcus Game class
from Board import Board
from ViewController import ViewController
from Player import Player

class Game:
    
    def __init__(self, rows = 6, columns = 7, winBy = 4, numberOfSpaces = 0):
        self.winBy = winBy #we have a winby condition
        self.rows = rows
        self.columns = columns
        self.view = ViewController(Board(self.rows,self.columns, self.winBy), numberOfSpaces)
        self.isOver = False #not over, automatically running
        self.turnNumber = 0 #number set to 0 at first.
        self.playerList = [] #no players at first.

        Player.numberOfPlayers = 0

        self.playerList.append(Player())
        self.playerList.append(Player()) #by default we have two players.




    



