import screen
import tkinter
import game
from threading import Timer
from time import sleep
class Controller:

    def __init__(self):
        cu = 5
        width = 600
        self.__root = tkinter.Tk()
        self.__screen = screen.Screen(self.__root, height=width, width=width, columns=cu, raws=cu)
        tkinter.Button(self.__root, text="Quit", command=self.__quit, bg='#d8d3cb').pack(fill=tkinter.X )
        self.__game   = game.Game(columns=cu, raws=cu)
        self.__play   = True
        self.__interval = 0.5
        self.__input_pipe = { 0 : AIInputPipe(self.__game, 0 , 1,) , 1 : ClickerInputPipe(1, self.__screen.getCanvas(), self )}
        self.__id_hash = {}
        self.__running = True
        self.__root.update_idletasks()
        self.__root.update()

    def start(self):
        self.__drawerTread = Timer(self.__interval, self.mainloop)
        self.__ioTread     = Timer(self.__interval, self.ioloop)
        self.__drawerTread.start()
        self.__ioTread.start()
        self.__root.mainloop()

    def ioloop(self):
        while self.__running :
            player = self.__game.get_current_player()
            _input = self.__input_pipe[player]()
            while self.__running and not self.__game.make_move( _input  ):
                _input = self.__input_pipe[player]()
            sleep(self.__interval)

    def mainloop(self):
        while self.__running :
            self.draw()
            sleep(self.__interval)
            if self.__game.get_winner() != None :
                self.draw()
                self.__quit()


    def draw(self):
        while self.__game.stacklen() > 0 :
            column, raw, _id,  player = self.__game.stackpop()
            self.__id_hash[_id]  =  self.__screen.drawTool(column, 0, player)
            self.__screen.animate(self.__id_hash[_id], column, raw)

    def __quit(self):
        self.__running = False
        self.__ioTread.join(timeout=1)
        self.__drawerTread.join(timeout=5)
        #self.dra
        self.__root.destroy()
    def running(self):
        return self.__running

class InputPipe:

    def __init__(self , player):
        self.player = player
        self.i = 0
    def __call__(self):
        pass



class ClickerInputPipe(InputPipe):
    def __init__(self, player, canvas, controller):
        super().__init__(player)
        self.__canvas = canvas
        self.__controller = controller
        self.notclicked = True
        self.ret = 0

    def onClick(self , event):
        self.notclicked = False
        self.ret = self.__canvas.Xconvert(event.x)

    def __call__(self):
        self.__canvas.bind("<Button-1>", self.onClick)

        while self.__controller.running() and self.notclicked:
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

import ai

class AIInputPipe(InputPipe):
    def __init__(self, game, player, enemy):
        super().__init__(player)
        self.__game = game
        self.__enemy = enemy
    def __call__(self):
        winer , op = ai.GameBackTrack(self.__game, self.player, self.__enemy).back_track()
        if winer == self.__enemy :
            return randint(0 , 9)
        else :
            return op
        self.i += 1
