class AI:


    def find_legal_move(self, g, func, timeout=None):
        pass
from copy import deepcopy
class GameBackTrack:
    def __init__(self, game, player, enemy):
        self.__player = player
        self.__enemy = enemy
        self.__game = game
        self.__opthions = range(5)#game.__opthions

    def back_track(self , depth=4):
        winer = self.__game.get_winner()
        if depth == 0:
            winer = self.__player
        op = 0
        if winer == None:
            for op in self.__opthions:
                game = deepcopy(self.__game)
                if game.make_move( op ) :
                    winer , path = GameBackTrack(game , self.__enemy, self.__player).back_track(depth - 1)
                if winer == self.__player :
                    return winer , op #[op] + path
        return winer , op
