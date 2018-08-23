def convert_spoon_to_cup(x):
    return float(x / 1.5)

import operator

def calculate_mathematical_expression(x, y, expression):
    return float({  "-" : operator.__sub__ ,
                    "+" : operator.__add__ ,
                    "*" : operator.__mul__ , 
                    "/" : operator.__truediv__ }[expression](x ,y))

def calculate_from_string(_str="1+1"):
    
    parameters = [ "" ]
    operatorsSet = set("+-/*")
    for char in _str:
        if char not in operatorsSet:
            parameters[-1] += char
        else :
            parameters.append(char)
            parameters.append("")
    return calculate_mathematical_expression(float(parameters[0]),
                                             float(parameters[2]),
                                             parameters[1])


def largest_and_smallest(a, b, c):
    retTuple = []
    for ret , op in zip([a , a] , [ operator.__ge__ , operator.__le__ ] ):
        for x in [a , b ,c ] :
            ret = x if op(x, ret) else ret 
        retTuple.append(ret)
    return tuple(retTuple)


import math

def quadratic_equation(a ,b ,c):
    delta = b ** 2 - 4 * a * c
    if delta < 0 :
        return None , None
    if delta == 0 :
        return - b / (2 * a) , None
    else :
        return [ ( op(- b, math.sqrt(delta )) ) / ( 2 * a) for op in [ operator.__add__ , operator.__sub__ ] ]

def quadratic_equation_user_input():
    print("Insert coefficients a, b, and c:")    a , b , c = (float(input()) for _ in range(3))    solutions = quadratic_equation(a , b , c)
    print(solutions)
    output = {  2 : "The equation has 2 solutions: {0} and {1}",
                1 : "The equation has 1 solutions: {0}",
                0 : "The equation has no solutions" } [ 
                    sum(  [1 if str(sol) != 'nan' else 0 for sol in solutions]  )
                  ].format ( *[sol for sol in solutions if str(sol) != 'nan'] ) 
    print (output)

from functools import reduce

def shapes():
    def getInput(i):
        return [ float(input()) for _ in range(i) ] 

    def circle ():
        return getInput(1)[0] ** 2 * math.pi
    def rectangle():
        return reduce( lambda x , y : x * y , getInput(2) )
    def trapezoid ():
   
        def _f(x, y):
            return (x[0] + x[1]) * y / 2 if isinstance(x , tuple) else (x ,y)

        return reduce (_f , getInput(3) )

    
    return (
        lambda g : g() if g != None else None)  ({
                
            1 : circle,
            2 : rectangle,
            3 : trapezoid
        
    }.get(int(input("Choose shape (1=circle, 2=rectangle, 3=trapezoid):"))))

def temperature():
    pass

def is_it_summer_yet(temp, a, b, c):
    return sum([ 1 if x > temp else 0 for x in (a , b , c)]) > 1
   



def run():
    #print(largest_and_smallest(4 , 1 , 10))
    #print(calculate_from_string("7*9"))
    #print(quadratic_equation(1 , 1.5 , -1))
    #quadratic_equation_user_input()
    #print(shapes())
    print (is_it_summer_yet(20,21,22,20))