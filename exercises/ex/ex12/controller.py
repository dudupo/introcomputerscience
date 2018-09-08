import screen
import tkinter
import game
from threading import Timer
from time import sleep
class Controller:

    def __init__(self):
        cu = 10
        width = 600
        self.__root = tkinter.Tk()
        self.__screen = screen.Screen(self.__root, height=width, width=width, columns=cu, raws=cu)
        self.__game   = game.Game(columns=cu, raws=cu)
        self.__play   = True
        self.__interval = 0.5
        self.__input_pipe = { 0 : RandomInputPipe(0) , 1 : ClickerInputPipe(1 , self.__screen.getCanvas())}
        self.__id_hash = {}
        cu = 10
        self.__root.update_idletasks()
        self.__root.update()

    def start(self):
        Timer(self.__interval, self.mainloop).start()
        Timer(self.__interval, self.ioloop).start()
        self.__root.mainloop()

    def ioloop(self):
        player = self.__game.get_current_player()
        _input = self.__input_pipe[player]()
        while not self.__game.make_move( _input  ):
            _input = self.__input_pipe[player]()
        sleep(self.__interval)
        self.ioloop()

    def mainloop(self):
        self.draw()
        sleep(self.__interval)
        self.mainloop()

    def draw(self):
        while self.__game.stacklen() > 0 :
            column, raw, _id,  player = self.__game.stackpop()
            self.__id_hash[_id]  =  self.__screen.drawTool(column, 0, player)
            self.__screen.animate(self.__id_hash[_id], column, raw)


class InputPipe:

    def __init__(self , player):
        self.player = player
        self.i = 0
    def __call__(self):
        pass



class ClickerInputPipe(InputPipe):
    def __init__(self, player, canvas):
        super().__init__(player)
        self.__canvas = canvas
        self.notclicked = True
        self.ret = 0

    def onClick(self , event):
        self.notclicked = False
        self.ret = self.__canvas.Xconvert(event.x)

    def __call__(self):
        self.__canvas.bind("<Button-1>", self.onClick)

        while self.notclicked:
            sleep( 0.1 )
        self.notclicked = True
        return self.ret


from random import randint
class RandomInputPipe(InputPipe):
    def __init__(self, player):
        super().__init__(player)

    def __call__(self):
        self.i += 1
        return randint(0 , 9)
