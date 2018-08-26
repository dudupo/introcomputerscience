
# file_name : crossword.py


from copy import deepcopy , copy


def matrix2dgen(matrix):
    for j , line in enumerate( matrix ):
        for i , X in enumerate( line ) :
            yield (i , j , 0) , X

def cube3dgen(cube):
    for k , matrix in enumerate( cube ) :
        for j , line in enumerate( matrix ):
            for i , X in enumerate( line ) :
                yield (i , j , k) , X

def crossword( matrix , wards , directionsstring , output_file , matrixgen=matrix2dgen , directions3dstring='a'):

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
        'd' : ( lambda i , j , k : (i , j + 1     , k )) ,
        'l' : ( lambda i , j , k : (i + 1 , j     , k )) ,
        'w' : ( lambda i , j , k : (i - 1 , j + 1 , k )) ,
        'y' : ( lambda i , j , k : (i + 1 , j + 1 , k))
    }


    def permutation( arr , places ):
        return arr[places[0]] , arr[places[1]] , arr[places[2]]

    directions3d = {
        'a' : (lambda i , j , k , f : permutation(f(i , j , k) , [0, 1, 2])),
        'b' : (lambda i , j , k , f : permutation(f(i , k , j) , [0, 2, 1])),
        'c' : (lambda i , j , k , f : permutation(f(j , k , i) , [2, 0, 1]))
    }
    
    directions3d = { key : value for key , value in directions3d.items() \
     if key in directions3dstring }

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
                for direction3d , g in directions3d.items():
                    defaultstate[ward[0]].append (  (iter(ward[1:]) , direction3d , direction))

    automat =  { }
    for position , X in matrixgen(matrix):
        automat[position] = deepcopy(defaultstate)

    for position , X in matrixgen(matrix):
        state = automat[position]
        if X in state :
            for _nextgen , direction3d , direction in state[X] :
                _nextgen = copy(_nextgen)
                _next = next( _nextgen )
                if _next == '$':
                    out[next(_nextgen)] += 1
                else:
                    _nextposition = directions3d[direction3d]( *position ,   directions[direction] )
                    if _nextposition in automat :
                        automat[ _nextposition ][ _next ] = [ ] \
                         if _next not in automat[_nextposition] else automat[_nextposition][_next]
                        automat[ _nextposition][ _next ].append( (copy( _nextgen ) , direction3d ,  direction)  )

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
