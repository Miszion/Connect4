#Mission's Board class makes a blank board. 
class Board:
    
    def __init__(self, rows, columns, winBy = 4): #this will initialize the playing board
        self.grid = list() #we have a 1D list.
        self.rows = rows
        self.columns = columns
        self.winBy = winBy #designate a win-by condition.

        for i in range(0, rows): #append how many rows
           self.grid.append(list())

        for a in range(0, rows):
            for b in range(0, columns):
                self.grid[a].append(None) #make the rows into nothing (yet)

    def clear(self): #clears the board. Reinitializes the board.
        self.grid = list()
        for i in range(0, rows):
           self.grid.append(list())

        for a in range(0, rows):
            for b in range(0, columns):
                self.grid[a].append(None)


    def checkIfWinner(self, chip): #checks the winner

        #check vertical first

        if (self.checkVertical(chip) or self.checkHorizontal(chip) or self.checkLeftDiagonal(chip) or self.checkRightDiagonal(chip)):
            return True
        else:
            return False

    def checkVertical(self, chip):
        count = 0

        for i in range(chip.row, self.rows): #check vertical first, only have to check below...
            if (self.grid[i][chip.column] != None):
                if (self.grid[i][chip.column].color is chip.color):
                    count = count + 1
                else:
                    break
            else:
                break

        if (count == self.winBy):
            print("Player " + str(chip.playerID) + " Wins!", end = " ")
            return True
        else:
            return False

    def checkHorizontal(self, chip):
        count = 1

        for i in range(chip.column + 1, self.columns): #check right hand side, breaks if it isnt the chip color
            if (self.grid[chip.row][i] != None):
                if (self.grid[chip.row][i].color is chip.color):
                    count = count + 1
                else:
                    break
            else:
                break
      
        for i in range(chip.column - 1, -1, -1): #check left hand side.
            if (self.grid[chip.row][i] != None):
                if (self.grid[chip.row][i].color is chip.color):
                    count = count + 1
                else:
                    break
            else:
                break

        if (count >= self.winBy): #this is minus one because the chip is checked the same from both sides.
            print("Player " + str(chip.playerID) + " Wins!", end = " ")
            return True
        else:
            return False

    def checkRightDiagonal(self, chip): #this will check both directions of the right diagonal.
        count = 1

        for i in range(1,self.winBy): #win by condition is set to 4 automatically.
            if ((chip.row- i >= 0) & (chip.column + i < self.columns)):
                if (self.grid[chip.row- i][chip.column + i] != None):
                    if (self.grid[chip.row-i][chip.column+ i].color is chip.color):
                                count = count + 1
                    else:
                        break
                else:
                    break
        for i in range(1,self.winBy):
            if ((chip.row + i < self.rows) & (chip.column - i >= 0)):
                if (self.grid[chip.row+i][chip.column - i] != None):
                    if (self.grid[chip.row+i][chip.column - i].color is chip.color):
                        count = count + 1
                    else:
                        break
                else:
                    break

        if (count == self.winBy):
            print("Player " + str(chip.playerID) + " Wins!", end = " ")
            return True
        else:
            return False


    def checkLeftDiagonal(self, chip):
        count = 1
        for i in range(1, self.winBy):
            if ((chip.row -i >= 0) & (chip.column -i >= 0)):
                if (self.grid[chip.row -i][chip.column - i] != None):
                    if (self.grid[chip.row-i][chip.column -i].color is chip.color):
                        count = count + 1
                    else:
                        break
                else:
                    break

        for i in range(1, self.winBy):
            if ((chip.row +i < self.rows) & (chip.column +i < self.columns)):
                if (self.grid[chip.row +i][chip.column + i] != None):
                    if (self.grid[chip.row+i][chip.column +i].color is chip.color):
                        count = count + 1
                    else:
                        break
                else:
                    break
        if (count == self.winBy):
            print("Player " + str(chip.playerID) + " Wins!", end = " ")
            return True
        else:
            return False


        




