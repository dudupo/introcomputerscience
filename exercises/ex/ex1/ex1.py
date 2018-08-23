
#file_name : hello_turtle.py 

import turtle

def draw_petal(agent = turtle.Turtle(), steps=30):
    
    for i in range(4):
        agent.forward(steps)
        agent.right( (45 + 90*i ) % 180 )

def draw_flower(agent = turtle.Turtle() , steps = 30):
    draw_petalWarper = lambda : draw_petal(agent, steps)
    agent.left(45)

    for _ in range(4):
        draw_petalWarper()
        agent.left(90)

    agent.left(45)
    agent.forward(90)    

def draw_flower_advanced(agent = turtle.Turtle() , steps = 30):
    draw_flower(agent, steps)

    agent.up()

    for _ in range(2):
        agent.right(90)
        agent.forward(150)
    
    agent.left(90)
    agent.down()

def draw_flower_bed(agent = turtle.Turtle() , steps = 30):
    agent.up()
    agent.forward(200)
    agent.left(180)
    agent.down()

    for _ in range(3):
        draw_flower_advanced(agent, steps)

#file_name : math_print.py

import math

def golden_ratio(n = 10):
    
    def _golden_ratio(n = 10):
        if n == 0:
            return 1 
        return 1 + 1 / _golden_ratio(n-1)

    print(_golden_ratio(n))

def six_squre():
    print ( 6 ** 2)

def hypotenuse():
    print ( math.sqrt( 5 ** 2 + 12 ** 2  ))

def pi ():
    print ( math.pi )



def run():
    #draw_flower_bed()
    #turtle.done()
    golden_ratio(30)
    six_squre()
    hypotenuse()
    pi()