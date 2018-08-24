
# file_name : crossword.py


'''
    automat[(i , j)][X] -> True , directions, Y
                        -> False, None, None
                        -> True , None, $
'''

def crossword( matrix , wards , directionsstring , output_file):

    thereisoppsite = False
    opposite =  {'r' : 'l' , 'u' : 'd' ,'x' : 'y' , 'z' : 'w' }
    for direction in directionsstring:
        if direction in opposite :
            directionsstring += opposite[direction]
            thereisoppsite = True

    def reverseward(ward):
        if len(ward) > 1 :
            return ward[-1] + reverseward(ward[:-1])
        else :
            return ward[-1]

    if thereisoppsite :
        wards += [ reverseward(ward) for ward in wards ]

    directions = {
        'd' : ( lambda i , j : i , j - 1 ) ,
        'l' : ( lambda i , j : i + 1 , j ) ,
        'y' : ( lambda i , j : i - 1 , j - 1 ) ,
        'w' : ( lambda i , j : i + 1 , j + 1 )
    }
    directions = { key : value for key , value in directions.items() \
     if key in directionsstring }
    wards = [ ward + '$' for ward in wards ]
    defaultstate = { ward[0] : (ward[1] , direction) \
     for direction , f in directions.items() for ward in wards }

    automat =  { }
    for j , X in enumerate( line )  :
        for i , line in enumerate( matrix ) :
            state = automat[(i , j)] if (i , j) in automat else defaultstate
            if X in state :
                for direction , _next  in state[X] :
                    if _next == '$':
                        pass # updade
                    else:
                        _i , _j = directions[direction]( i , j )
                        automat[ (_i , _j) ] = { } \
                         if (_i , _j) not in automat else automat[(_i , _j)]
                        automat[ (_i , _j) ][ _next ] = [ ] \
                         if _next not in automat[(_i , _j)] else automat[(_i , _j)][_next]
                        automat[ (_i , _j)][ _next ].append( direction , next( _next ) )

import os

if __name__ == '__main__':
    args = os.sys.argv
    if len(args) > 4 :
        wards  = [ line for line in open( args[1] ).read() ]
        matrix = [ [ X for X in line ]  for line in open(args[2]).read() ]
        querydirection = args[4]
    else :
        print ("ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions.")
