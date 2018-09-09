from copy import deepcopy
from ex5 import crossword

class State:
    def __init__(self, columns, raws, playerscount):
        self.__playerscount = playerscount
        self.__columns = columns
        self.__raws = raws
        self.__matrix = [ [ "None" for raw in range(self.__raws) ] for column in range(self.__columns) ]

    def updateState(self, col, raw, player):
        new_state = deepcopy( self )
        new_state.__matrix[col][raw] = "{0}".format( player )
        return new_state

    def get_winner(self):
        wards = ["{0}".format( player ) * 4 for player in range(self.__playerscount)]
        directionsstring = 'dlwy'
        winers = crossword(self.__matrix, wards , directionsstring)
        for playerseq , count in winers.items():
            if count > 0 :
                return int(playerseq[0])
        return None

    def get_player_at(self, row, col):
        return int(self.__matrix[col][row]) if self.__matrix[col][row] != None else None
