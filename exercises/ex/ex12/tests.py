import logging
import screen
import controller
import time
import tkinter
import threading
def loadScreen(width = 600, cu=10 ):
    logging.info(' > function -> loadScreen ')
    __root = tkinter.Tk()
    __screen = screen.Screen(__root, height=width, width=width, columns=cu, raws=cu)
    _id = __screen.drawTool( 1 , 1 ,player=0)
    print(_id)
    __screen.drawTool(3 ,5 , player=0)
    __screen.drawTool(3 ,6 , player=1)
    __screen.drawTool(6 ,5 , player=1)
    logging.info( ' > exit function ( loadScreen )')
    __screen.animate(_id , 1 , 5)
    def loop():
        threading.Timer(loop, 5).start()

    loop()
    threading.Timer(__root.mainloop(), 5).start()

def TestController():
    controller.Controller().start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    #loadScreen()
    TestController()
    # controller.Controller().start()
    # loggeing.debug('debug message')
    # loggeing.info('info message')
    # loggeing.warn('warn message')
    # loggeing.error('error message')
    # loggeing.critical('critical message')
