#Mission Marcus Main Class.
from Player import Player
from Board import Board
from ViewController import ViewController
from GameController import GameController


def main():

    gameCont = GameController() #set up a game controller/

    gameCont.playGame() #play the game.

if __name__ == "__main__": #check if the file is main.
    main()