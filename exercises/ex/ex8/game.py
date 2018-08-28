############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction
from board import Board

############################################################
# Class definition
############################################################


class Game:
    """
    A class representing a rush hour game.
    A game is composed of cars that are located on a square board and a user
    which tries to move them in a way that will allow the red car to get out
    through the exit
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board
        for i in range(gh.get_num_cars()):
            self.board.add_car(Car(*gh.get_car_input(board.size)))
    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Print board to the screen
            2. Get user's input of: what color car to move, and what direction to
                move it.
            2.a. Check the the input is valid. If not, print an error message and
                return to step 2.
            2. Move car according to user's input. If movement failed (trying
                to move out of board etc.), return to step 2.
            3. Report to the user the result of current round ()
        """


        print(self.board)
        color = input("What color car would you like to move?")
        while not self.board.move(color ,  gh.get_direction()):
            print("Illegal move, try again")
            color = input("What color car would you like to move?")

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while not self.board.Win:
            self.__single_turn()
        print("Congratulations! you released the red car!")

############################################################
# An example usage of the game
############################################################
if __name__=="__main__":

    car1 =  Car('R', 3 , [0,0], 1)
    car2 =  Car('B', 2 , [1,1], 0)

    board = Board([], [5,3]) # if using a dictionry of cars. use '[]' if using a list
    game = Game(board)
    game.play()
