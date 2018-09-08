class Game:

    @staticmethod
    def playersGenerator(playerscount):
        while True:
            for _ in range(playerscount):
                yield _

    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2

    def __init__(self, raws, columns, playerscount = 2):
        self.__raws , self.__columns = raws , columns
        self.__stack = []
        self.__i = 0
        self.__playersGen = Game.playersGenerator(playerscount)
        self.__player = next( self.__playersGen )
        self.rawof = [ raws - 1 for column in range(columns) ]

    def make_move(self, column):
        if self.rawof[column] >= 0 :
            self.__stack.append( ( column, self.rawof[column], self.genid(), self.__player ) )
            self.__i += 1
            self.__player = next(self.__playersGen)
            self.rawof[column] -= 1
            return True
        return False

    def get_winner(self):
        pass

    def get_player_at(self, row, col):
        pass

    def get_current_player(self):
        return self.__player

    def genid(self):
        return "p{0}:{1}".format(self.__player , self.__i)

    def stackpop(self):
        return self.__stack.pop(0)
    def stacklen(self):
        return len(self.__stack)
