
from screen import Screen


screen_min_x = Screen.SCREEN_MIN_X
screen_min_y = Screen.SCREEN_MIN_Y
screen_max_y = Screen.SCREEN_MAX_Y
screen_max_x = Screen.SCREEN_MAX_X

from math import acos , degrees , cos , sin , radians

from functools import reduce

class Vector:
    def __init__ (self, x=[0,0]):
        self.x = x

    def __add__ (self, other):
        return Vector(x = [x + y for x, y in zip(self.x , other.x) ])
    def __sub__ (self, other):
        return Vector(x = [x - y for x, y in zip(self.x , other.x) ])
    def dis (self):
        return sum( x ** 2 for x in self.x ) ** 0.5
    def __mul__ (self , other):
        return Vector(x=[ x * y for x , y in zip(self.x , other.x) ])
    def __call__ (self):
        return self.x
    def __contains__ (self , other):
        return reduce( lambda i , j : i and j ,
         [abs(y) < abs(x) for x , y in zip(self.x , other.x)])
    def __mod__ (self ,other):
        return Vector(x = [x % y if y != 0 else 0 for x , y in zip(self.x , other.x) ])
    def angle(self):
        ret = degrees(acos(self.x[0]  / self.dis()))
        return ret if self.x[1] > 0 else 360 - ret
    def rotate(self, alpha):
        alpha = radians(alpha)
        x , y = self.x[0] , self.x[1]
        return Vector ( x=[x * cos(alpha) - y * sin(alpha) , x * sin(alpha) + y * cos(alpha)])


class GameObj:
    def __init__ (self, location, speedvec,  _screen):
        self.location = Vector( x = location )
        self.speedvec = Vector( x = speedvec )
        self._screen = _screen
        self.widthVec = Vector(x =[ screen_max_x - screen_min_x ,
         screen_max_y - screen_min_y] )
        self.Ovec = Vector(x=[screen_min_x, screen_min_y] )
        self.radius = float(1)

    def step(self):
        self.location += self.speedvec
        self.location = ((self.location - self.Ovec)  % self.widthVec) + self.Ovec

    def _in (self, _GameRunner):
        return self.location in Vector([_GameRunner.screen_max_x,
         _GameRunner.screen_max_y]  )

    #abstract
    def draw(self):
        pass

    def left(self ,_degrees):
        #self.location = self.location.rotate(_degrees)
        self.speedvec = self.speedvec.rotate(_degrees)

    def right(self , _degrees):
        #self.location = self.location.rotate(360 - _degrees)
        self.speedvec = self.speedvec.rotate(- _degrees)

    def has_intersection(self , otherobj):
        if self == otherobj :
            return False
        return (otherobj.location - self.location).dis() <= self.radius + otherobj.radius

    #abstract
    def intersection (self):
        return True

    def accelerate(self) :
        self.speedvec += Vector(x=[cos(radians(self.speedvec.angle())),
           sin(radians(self.speedvec.angle()))])
    def decelerate(self):
        self.speedvec -= Vector(x=[cos(radians(self.speedvec.angle())),
           sin(radians(self.speedvec.angle()))])
    def refflocation(self , perent):
        return perent.location + reduce( lambda v , u : v + u ,
         [ self.speedvec for _ in range( max(int(perent.radius + 1) , int(self.radius+1)))])

from random import randint , choice , uniform
class Ship(GameObj) :
    def __init__ (self , _screen):
        super().__init__((7,30) , (1,1) , _screen)
        self.life = 3
    def draw(self):
        x,y = self.location.x
        self._screen.draw_ship(x,y, self.speedvec.angle())

    def step(self):
        super().step()

    def intersection(self):
        if self.life > 1 :
            self._screen.show_message("~WARNING: " , "SpaceShip have been hitted")
            self._screen.remove_life()
            self.life -= 1
            return True
        else :
            self._screen.show_message("~Sorry: " , "SpaceShip have been destroyed")
            self._screen.remove_life()
            self.life -= 1
            return False

class Asteroid(GameObj):
    def __init__ (self, location, speedvec, size,  _screen):
        super().__init__(location, speedvec, _screen)
        self.size = size
        self._screen.register_asteroid(self , self.size)
        self.radius = self.size * 10 - 5

    def draw(self):
        x,y= self.location.x
        self._screen.draw_asteroid(self ,x,y)
    def step(self):
        super().step()

    def intersection(self):
        return False
    def splitting(self ,_torpedo) :
        ret = []

        speedvec = (self.speedvec + _torpedo.speedvec) * \
         Vector(x = [1 / self.speedvec.dis() for _ in range(2)])

        if self.size > 1 :
            for _ in range(2):
                ret.append(
                 Asteroid(location=self.location.x,
                  speedvec=speedvec.x,
                   size=self.size - 1
                   , _screen=self._screen))

            ret[-1].speedvec = Vector(x=[-1,-1] ) * ret[0].speedvec
            ret[-1].location = ret[-1].refflocation(self)
            ret[0].location = ret[0].refflocation(self)
        return ret


class Torpedo( GameObj ):
    def __init__ (self , _screen , _ship):
        self.live = 200
        self.radius = 4
        location = _ship.location + reduce( lambda v , u : v + u ,
         [ _ship.speedvec for _ in range( max(int(_ship.radius + 1) , self.radius+1)) ])

        super().__init__( location.x  , _ship.speedvec.x , _screen)

        self.ship = _ship
        self.accelerate()
        self.accelerate()

    def has_intersection(self , otherobj):
        if self == otherobj :
            return self.live < 0
        else :
            return super().has_intersection(otherobj)

    def draw(self):
        x,y= self.location.x
        self._screen.draw_torpedo(self ,x,y , self.speedvec.angle())

    def step(self):
        self.live -= 1
        super().step()

    def intersection(self):
        return False
