#Mission Marcus Player Class.
from Chip import Chip

class Player:
    numberOfPlayers = 0
    listOfColors = ["R", "B", "G", "Y", "P", "O"] #up to 6 possible chip colors. 
    def __init__(self):
        self.name = "Player " + str(Player.numberOfPlayers + 1)
        self.id = Player.numberOfPlayers #technically ID is 0
        self.color = Player.listOfColors[self.id]
        Player.numberOfPlayers = Player.numberOfPlayers + 1
        self.chipCount = 56


    def makeMove(self, view, col):
            
        if( self.chipCount > 0):

            for r in range(view.board.rows-1, -1, -1):
                if ((view.board.grid[r][col] == None)):
                    c1 = Chip(self.id, r, col, self.color)
                    view.board.grid[r][col] = c1 #make a chip at that area.
                    self.chipCount = self.chipCount - 1 #subtract a chip
                    view.display()
                    return view.board.checkIfWinner(c1) #check board at that position
        else:
            print(self.name + " has run out of chips!")
