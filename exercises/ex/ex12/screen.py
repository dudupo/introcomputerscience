import tkinter

class MatrixCanvas(  tkinter.Canvas  ):
    def __init__(self, masterroot, raws, columns, width, height ):
        super().__init__(masterroot, height=height, width = width)
        self.__MatrixCanvasWidth    = width
        self.__MatrixCanvasHeight   = height
        self.__MatrixCanvasRaws     = raws
        self.__MatrixCanvasColumns  = columns

    def convertX(self, x):
        return x * ( self.__MatrixCanvasWidth / self.__MatrixCanvasRaws  )
    def convertY(self, y):
        return y * (self.__MatrixCanvasHeight / self.__MatrixCanvasColumns )
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
    def create_oval(self, color ='black', *args) :
        x0 , y0 = args
        x1 , y1 = x0 + 1 , y0 + 1
        return super().create_oval(self.convertArray(x0, y0, x1, y1), color=color)

class Screen:

    def __init__(self, root, width = 600, height=600 , raws = 8, columns = 8):
        self.__root     = root
        self.__canvas   = MatrixCanvas(self.__root, raws, columns, width, height)
        self.__columns  = columns
        self.__raws     = raws
        self.colors = { 0 : 'black' , 1 : 'red' }
        self.drawMatrix()

    def drawMatrix(self):
        for i in range(self.__columns):
            self.__canvas.create_line( i, 0, i, self.__raws)
        for j in range(self.__raws):
            self.__canvas.create_line( 0, j, self.__columns, j)

        #C.create_oval( (width / cu) * 4 , (width / cu) * 4  , (width / cu) * 5 , (width / cu) * 5  )
        self.__canvas.pack()

    def getColor(self, player):
        return self.colors[player]
    def drawTool(self, x, y, player=0):
        self.__canvas.create_oval(x, y, color = self.getColor(player))
