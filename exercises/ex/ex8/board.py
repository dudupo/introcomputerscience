############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction

############################################################
# Constants
############################################################

# place your constants here

############################################################
# Class definition
############################################################


class Board():
    """
    A class representing a rush hour board.
    """

    def __init__(self, cars, exit_board, size=6):

        self.state = [ ["-" for _ in range(size)] for __ in range(size)]
        self.size = size
        self.state[exit_board[0]][exit_board[1]] = 'E'

        self.Win = False

        self.cars = { }
        for car in cars :
            self.add_car(car)

        self.exit_board = exit_board
        self.size = size
        """
        Initialize a new Board object.
        :param cars: A list (or dictionary) of cars.
        :param size: Size of board (Default size is 6).
        """
        # implement your code here (and then delete the next line - 'pass')
        pass



    def legal(self, car):
        for x , y in car:
            if not self.is_empty((x,y)):
                return False
        return True

    def add_car(self, car):
        if self.legal(car):
            for x , y in car :
                self.state[x][y] = car.color
            self.cars[car.color] = car

    def is_empty(self, location):
        x , y = location
        return not( x < 0 or y < 0 or x >= self.size or y >= self.size or self.state[x][y] != '-')


        """
        Check if a given location on the board is free.
        :param location: x and y coordinations of location to be check
        :return: True if location is free, False otherwise
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

    def move(self, color, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False otherwise.
        """
        if color in self.cars:
            car = self.cars[color]
            x , y = car.location
            if direction != 0 :
                _x , _y = 0 , 0
                if car.orientation:
                    if direction ==  Direction.RIGHT :
                        if not self.is_empty( (x , y + car.length) ):
                            return False
                        else :
                            self.state[x][y] = "-"
                            _x , _y = x , y + car.length
                            car.location = x , y + 1
                    elif direction == Direction.LEFT :
                        if not self.is_empty( (x , y - 1) ):
                            return False
                        else :
                            self.state[x][y + car.length - 1 ] = "-"
                            _x , _y = x , y - 1
                            car.location = x , y - 1
                    else:
                        return False
                else :
                    if direction == Direction.DOWN:
                        if not self.is_empty( (x + car.length  , y) ):
                            return False
                        else :
                            self.state[x][y] = "-"
                            _x , _y = x + car.length  , y
                            car.location = x + 1 , y
                    elif direction == Direction.UP :
                        if not self.is_empty( (x - 1  , y) ):
                            return False
                        else :
                            self.state[x + car.length - 1][y] = "-"
                            _x , _y = x - 1  , y
                            car.location = x - 1 , y
                    else :
                        return False

                if self.state[_x][_y] == 'E':
                    self.Win = True

                self.state[_x][_y] = car.color
            return True
        return False

    def __repr__(self):
        ret = ""
        for row in self.state:
            for c in row:
                ret += " {0} ".format(c)
            ret += "\n"
        return ret

        """
        :return: Return a string representation of the board.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass
