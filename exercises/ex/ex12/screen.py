import tkinter
from threading import Timer


class MatrixCanvas(  tkinter.Canvas  ):
    def __init__(self, masterroot, raws, columns, width, height ):
        super().__init__(masterroot, height=height, width = width)
        self.__MatrixCanvasWidth    = width
        self.__MatrixCanvasHeight   = height
        self.__MatrixCanvasRaws     = raws
        self.__MatrixCanvasColumns  = columns

    def convertX(self, x):
        return x * ( self.__MatrixCanvasWidth / self.__MatrixCanvasColumns  )
    def convertY(self, y):
        return y * (self.__MatrixCanvasHeight / self.__MatrixCanvasRaws )
    def Xconvert(self , x):
        return int( x * float(  self.__MatrixCanvasColumns  / self.__MatrixCanvasWidth))
    def Yconvert(self, y):
        return int( y * float( self.__MatrixCanvasRaws / self.__MatrixCanvasHeight ))
    def convertPoint(self, x, y):
        return self.convertX(x) , self.convertY(y)
    def convertArray(self, *args):
        ret = []
        for i in range(0, len( args ) ,2):
            x , y = self.convertPoint(args[i] , args[i+1])
            ret.append(x)
            ret.append(y)
        return ret
    def create_line(self, *args ):
        return super().create_line(self.convertArray(*args))
    def create_oval(self, *args) :
        x0 , y0 , color = args
        x1 , y1 = x0 + 1 , y0 + 1
        return super().create_oval(self.convertArray(x0, y0, x1, y1), outline=color, fill='#ceceb1')

class Screen:

    def __init__(self, root, width = 600, height=600 , raws = 8, columns = 8):
        self.__root     = root
        self.__canvas   = MatrixCanvas(self.__root, raws, columns, width, height)
        self.__columns  = columns
        self.__raws     = raws
        self.colors = { 0 : 'black' , 1 : 'red' }
        self.drawMatrix()
        self.__vx = 0
        self.__vy = (height / columns) / 5

    def drawMatrix(self):
        for i in range(self.__columns):
            self.__canvas.create_line( i, 0, i, self.__raws)
        for j in range(self.__raws):
            self.__canvas.create_line( 0, j, self.__columns, j)

        self.__canvas.pack()

    def getColor(self, player):
        return self.colors[player]
    def drawTool(self, x, y, player=0):
        color = self.getColor(player)
        return self.__canvas.create_oval(x, y, color)
    def getCanvas(self):
        return self.__canvas
    def animate(self, objId, x, y):
        x , y = self.__canvas.convertPoint(x , y)
        def dis(x0, y0, x1, y1):
            return ( (x1 - x0) ** 2 + (y1 - y0)**2 ) ** 0.5

        def _animate(objId, x, y, vx, vy):
            x0 , y0 , _ , __ = self.__canvas.coords( objId )
            if (x, y) != (x0, y0):
                self.__canvas.move( objId , vx , vy  )
                Timer(0.005, _animate, [objId, x, y, vx, vy]).start()

        _animate(objId, x, y, self.__vx, self.__vy)
    def Xconvert(self , x):
        return self.__canvas.Xconvert(x)
    def Yconvert(self, y):
        return self.__canvas.Yconvert(y)
