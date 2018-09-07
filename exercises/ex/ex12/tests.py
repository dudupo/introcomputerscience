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
    __screen.drawTool( 1 , 1 , 0)
    __screen.drawTool(3 ,5 , 0)
    logging.info( ' > exit function ( loadScreen )')
    #__root.mainloop()
    time.sleep(1)
    __root.destroy()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    loadScreen()

    # controller.Controller().start()
    # loggeing.debug('debug message')
    # loggeing.info('info message')
    # loggeing.warn('warn message')
    # loggeing.error('error message')
    # loggeing.critical('critical message')
