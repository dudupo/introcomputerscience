
# file_name : crossword.py


'''
    automat[(i , j)][X] -> True , directions, Y
                        -> False, None, None
                        -> True , None, $
'''



def crossword( matrix ):
    automat =  { }

    for i , line in enumerate( matrix ) :
        for j , X in enumerate( line )  :
            positive, directions, _next  = automat[(i , j)](X)
            if positive :
                if _next == '$':
                    pass # updade
                else:
                     
    pass

import os

if __name__ == '__main__':
    args = os.sys.argv
    if len(args) > 4 :
        wards  = [ line for line in open( args[1] ).read() ]
        matrix = [ [ X for X in line ]  for line in open(args[2]).read() ]
        querydirection = args[4]
    else :
        print ("ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions.")
