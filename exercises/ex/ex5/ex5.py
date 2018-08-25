
# file_name : crossword.py


'''
    automat[(i , j)][X] -> True , directions, Y
                        -> False, None, None
                        -> True , None, $
'''
from copy import copy

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

    out = { ward : 0 for ward in wards }
    wards = [ (ward , ward ) for ward in wards ]
    if thereisoppsite :
        wards += [ (reverseward(ward) , ward) for ward , x  in wards ]

    wards = [ list(_str) + ['$' ] +  [ward] for _str , ward in wards ]

    print(len(wards))

    directions = {
        'd' : ( lambda i , j : (i , j + 1 )) ,
        'l' : ( lambda i , j : (i + 1 , j )) ,
        'y' : ( lambda i , j : (i - 1 , j + 1 )) ,
        'w' : ( lambda i , j : (i + 1 , j - 1 ))
    }
    directions = { key : value for key , value in directions.items() \
     if key in directionsstring }

    defaultstate = { ward[0] :[ (iter(ward[1:]) , direction) \
     for direction , f in directions.items()] for ward in wards }

    print(defaultstate['d'])

    #print(defaultstate)
    automat =  { }
    for j , line in enumerate( matrix )  :
        for i , X in enumerate( line ) :
            state = automat[(i , j)] if (i , j) in automat else defaultstate
            if X in state :
                for _nextgen , direction in state[X] :
                    _nextgen = copy(_nextgen)
                    _next = next( _nextgen )
                    if _next == '$':
                        out[next(_nextgen)] += 1

                    else:
                        _i , _j = directions[direction]( i , j )
                        automat[ (_i , _j) ] = defaultstate \
                         if (_i , _j) not in automat else automat[(_i , _j)]
                        automat[ (_i , _j) ][ _next ] = [ ] \
                         if _next not in automat[(_i , _j)] else automat[(_i , _j)][_next]
                        automat[ (_i , _j)][ _next ].append( (copy( _nextgen ) , direction)  )

    with open(output_file, 'w') as _file :
        for ward , _count in out.items() :
            if _count > 0 :
                _file.write("{0} : {1}\n".format(ward, _count))

import os

if __name__ == '__main__':
    args = os.sys.argv
    if len(args) > 4 :
        wards  = [ line.rstrip('\n') for line in open( args[1] ).readlines() ]
        matrix = [ [ X for X in line.rstrip('\n') if X != ',' ]  for line in open(args[2]).readlines() ]
        print(matrix)
        crossword(matrix , wards , args[3] , args[4] )
    else :
        print ("ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions.")
