#Mission Marcus View Controller. this designates the views! Can easily be swapped out for an actual game board.
class ViewController:

    def __init__(self, board, numberOfSpaces = 0):
        self.board = board

        if (numberOfSpaces < 0):
            self.numberOfSpaces = 0
        else:
            self.numberOfSpaces = numberOfSpaces;


    def display(self):
        for z in range(0, self.board.rows): #Starts at 0, 0 so need to subtract one from given column

            for i in range(0,self.board.columns):
                print("+", end = "")
                for i in range(0, ((self.numberOfSpaces * 2) + 1)):
                    print("-", end = "")
            print("+")
            for w in range(0, self.board.columns):
                if (w == 0):
                    print ("+", end = "")
                    if (self.board.grid[z][w] == None):
                        for i in range(0, ((self.numberOfSpaces * 2) + 1)): #if the spot is unoccupied....
                            print(" ", end = "")
                    else:
                        for i in range(0, self.numberOfSpaces):
                            print(" ", end = "")
                        print(str(self.board.grid[z][w].color), end = "")
                        for i in range(0, self.numberOfSpaces):
                            print(" ", end = "")
                    print("|", end = "")
                else:
                    if (self.board.grid[z][w] == None):
                        for i in range(0, ((self.numberOfSpaces * 2) + 1)): #if the spot is unoccupied....
                            print(" ", end = "")
                    else:
                        for i in range(0, self.numberOfSpaces):
                            print(" ", end = "")
                        print(str(self.board.grid[z][w].color), end = "")
                        for i in range(0, self.numberOfSpaces):
                            print(" ", end = "")
                    print("|", end = "")
            print("")
        for i in range(0,self.board.columns):
                print("+", end = "")
                for i in range(0, ((self.numberOfSpaces * 2) + 1)):
                    print("-", end = "")
        print("+")
        for x in range(1, self.board.columns+1):
            if (x == 1):
                for i in range(0, self.numberOfSpaces + 1):
                    print(" ", end = "") 
            else:
                for i in range(0, (self.numberOfSpaces * 2) + 1):
                    print(" ", end = "")
            print(str(x), end = "")
        print(" ")
        print()
    
    
    def displayColumnAsk(self):
        print("Type the column in which you wish to move.")




