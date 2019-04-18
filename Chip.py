#Mission's Chip code defines what a chip is. It knows it's color and row and column.
class Chip:
    def __init__(self, playerID, row, column, color):
        self.color = color
        self.row = row
        self.column = column
        self.playerID = playerID + 1 #some book keeping to ensure players are numbered 1....n




