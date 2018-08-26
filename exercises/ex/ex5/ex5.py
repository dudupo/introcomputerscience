
# file_name : crossword.py


from copy import deepcopy , copy


def matrix2dgen(matrix):
    for j , line in enumerate( matrix ):
        for i , X in enumerate( line ) :
            yield (i , j) , X

def cube3dgenA(cube):
    for k , matrix in enumerate( cube ) :
        for (i , j) , X in matrix2dgen( matrix ) :
            yield (i , j , k) , X

def cube3dgenB(cube):
    for j in range(len( cube[0] )) :
        for k in range(len( cube )) :
            for i in range(  len(cube[0][0]) ) :
                yield (i , k , j) , cube[k][j][i]

def cube3dgenC(cube):
    for i in range(len( cube[0][0] )) :
        for k in range(len( cube )) :
            for j in range(  len(cube[0][0]) ) :
                yield (j , k , i) , cube[k][j][i]

def crossword( matrix , wards , directionsstring , output_file , matrixgen=matrix2dgen):

    thereisoppsite = False
    opposite =  {'r' : 'l' , 'u' : 'd' ,'x' : 'y' , 'z' : 'w' }
    rdirectionsstring = ""
    for direction in directionsstring:
        if direction in opposite :
            rdirectionsstring += opposite[direction]
            thereisoppsite = True

    def reverseward(ward):
        if len(ward) > 1 :
            return ward[-1] + reverseward(ward[:-1])
        else :
            return ward[-1]

    out = { ward : int(0) for ward in wards }
    wards = [ (ward , ward ) for ward in wards ]
    rwards = []
    if thereisoppsite :
        rwards = [ (reverseward(ward) , ward) for ward , x  in wards ]

    wards  = [ list(_str) + ['$' ] +  [ward] for _str , ward in wards ]
    rwards = [ list(_str) + ['$']  +  [ward] for _str , ward in rwards]

    directions = {
        'd' : ( lambda i , j : (i , j + 1 )) ,
        'l' : ( lambda i , j : (i + 1 , j )) ,
        'w' : ( lambda i , j : (i - 1 , j + 1 )) ,
        'y' : ( lambda i , j : (i + 1 , j + 1 ))
    }

    rdirections = { key : value for key , value in directions.items() \
     if key in rdirectionsstring }

    adirections = { key : value for key , value in directions.items() \
     if key in directionsstring }

    defaultstate = { }
    for _wards , _directions in zip([wards , rwards ] , [ adirections , rdirections ]) :
        for ward in _wards:
            if ward[0] not in defaultstate:
                defaultstate[ward[0]] = []
            for direction , f in _directions.items():
                defaultstate[ward[0]].append (  (iter(ward[1:]) , direction))

    automat =  { }
    for (i , j) , X in matrixgen(matrix):
        automat[(i , j)] = deepcopy(defaultstate)

    for position , X in matrixgen(matrix):
        state = automat[position]
        if X in state :
            for _nextgen , direction in state[X] :
                _nextgen = copy(_nextgen)
                _next = next( _nextgen )
                if _next == '$':
                    out[next(_nextgen)] += 1

                else:
                    _nextposition = directions[direction]( *position )
                    if _nextposition in automat :
                        automat[ _nextposition ][ _next ] = [ ] \
                         if _next not in automat[_nextposition] else automat[_nextposition][_next]
                        automat[ _nextposition][ _next ].append( (copy( _nextgen ) , direction)  )

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
        crossword(matrix , wards , args[3] , args[4] )
    else :
        print ("ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions.")
