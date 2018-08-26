from ex5 import crossword , cube3dgen
from copy import copy

import os

if __name__ == '__main__':
    args = os.sys.argv
    if len(args) > 4 :
        cube = []
        with open(args[2]) as _inputfile:
            matrix = []
            for line in _inputfile.readlines() :
                if line.rstrip('\n') != "***" :
                    matrix.append([ word for word in  line.rstrip('\n') if word != ','])
                else :
                    cube.append(copy (matrix))
                    matrix = []
            cube.append(copy (matrix))
        _inputfile.close()


        wards  = [ line.rstrip('\n') for line in open( args[1] ).readlines() ]

        directionsstring  = ""
        directions3dstring = ""

        for direction in args[3]:
            if direction in "abc" :
                directions3dstring += direction
            if direction in "rludxyzw":
                directionsstring += direction
        crossword(cube , wards , directionsstring , args[4] , matrixgen = cube3dgen , directions3dstring=directions3dstring )
    else :
        print ("ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions.")
