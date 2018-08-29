from screen import Screen
import sys
from gameobj import Ship , Asteroid , Torpedo

DEFAULT_ASTEROIDS_NUM = 5
from random import randint , choice , uniform
class GameRunner:
    MAXTORPEDOS = 1
    def __init__(self, asteroids_amnt):
        self._screen = Screen()
        self._torpedos = 0
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.ship = Ship(self._screen)
        self.objects  = [self.ship] + [
         Asteroid(location=(uniform(-400, 400),400),
          speedvec=(uniform(-1, 1),uniform(-3, -0.001)),
           size=randint(1 , 3) ,
            _screen=self._screen)  for _ in range(asteroids_amnt)]

        self.score = 0
    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def _game_loop(self):
        self._screen.set_score(self.score)

        if self.ship.life == 0:
            self._screen.show_message("~Sorry: " , "SpaceShip have been destroyed")
            self._screen.end_game()
        if len(self.objects) - self._torpedos - 1 == 0 :
            self._screen.show_message("~Congratulations: " , "You destroyed all asteroids")
            self._screen.end_game()
        if self._screen.should_end():
            self._screen.end_game()
        if self._screen.is_left_pressed():
            self.ship.left(7)
        if self._screen.is_right_pressed():
            self.ship.right(7)
        if self._screen.is_up_pressed():
            self.ship.accelerate()
        if self._screen.is_space_pressed() and \
         self._torpedos < GameRunner.MAXTORPEDOS  :
            _torpedo = Torpedo(self._screen, self.ship)
            self._screen.register_torpedo(_torpedo)
            self.objects.append(_torpedo)
            self._torpedos+=1

        for obj in self.objects:
            obj.step()

        removeObjs = []
        for iobj in self.objects:
            for jobj in self.objects:
                if iobj.has_intersection(jobj) :
                    if not iobj.intersection() :
                        removeObjs.append((iobj , jobj))

        for iobj , jobj in removeObjs:
            if iobj in self.objects :
                if isinstance(iobj , Asteroid):
                    self._screen.unregister_asteroid( iobj )
                elif isinstance(iobj , Torpedo) :
                    self._torpedos -= 1
                    self._screen.unregister_torpedo( iobj)
                    if isinstance(jobj , Asteroid):
                            self.score += {
                            1 : 100 ,
                            2 : 50 ,
                            3 : 20
                            }[ jobj.size ]

                            for child in jobj.splitting(iobj):
                                #self._screen.register_asteroid(children)
                                self.objects.append( child )

                self.objects.remove( iobj )



        for obj in self.objects:
            obj.draw()


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
