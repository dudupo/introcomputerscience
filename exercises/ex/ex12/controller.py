import screen
import tkinter
class Controller:

    def __init__(self):
        cu = 10
        width = 600
        self.__root = tkinter.Tk()
        self.__screen = screen.Screen(self.__root, height=width, width=width, columns=cu, raws=cu)
        self.__game   = None
        self.__play   = True


        coord = 10, 50, 240, 210
        #arc = C.create_arc(coord, start=0, extent=150, fill="red")

        cu = 10
        # for _ in range(cu):
        #     C.create_line((width / cu) * _ , 0, (width / cu) * _, width)
        #     C.create_line(0, (width / cu) * _ , width, (width / cu) * _)
        # C.create_oval( (width / cu) * 4 , (width / cu) * 4  , (width / cu) * 5 , (width / cu) * 5  )
        # C.pack()
    def start(self):
        self.__root.mainloop()

    def mainloop(self):
        self.__root.ontimer(self.mainloop, 5)
