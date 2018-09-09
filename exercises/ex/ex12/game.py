import state

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
        self.__nextplayer = { i : i + 1 for i in range(playerscount-1)}
        self.__nextplayer[playerscount - 1] = 0
        self.__player = 0
        self.rawof = [ raws - 1 for column in range(columns) ]
        self.__state = state.State(columns, raws, playerscount)

    def make_move(self, column):
        if self.rawof[column] >= 0 :
            self.__stack.append( ( column, self.rawof[column], self.genid(), self.__player ) )
            self.__state = self.__state.updateState(column, self.rawof[column], self.__player )
            self.__i += 1
            self.__player = self.__nextplayer[self.__player]
            self.rawof[column] -= 1
            return True
        return False

    def get_winner(self):
        return self.__state.get_winner()

    def get_player_at(self, row, col):
        return self.__state.get_player_at(raw, col)

    def get_current_player(self):
        return self.__player

    def genid(self):
        return "p{0}:{1}".format(self.__player , self.__i)

    def stackpop(self):
        return self.__stack.pop(0)
    def stacklen(self):
        return len(self.__stack)
