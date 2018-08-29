from ex11_backtrack import general_backtracking

def print_board(board, board_size=9):
    """ prints a sudoku board to the screen

    ---  board should be implemented as a dictinary
         that points from a location to a number {(row,col):num}
    """
    for row in range(board_size):
        if(row%3 == 0):
            print('-------------')
        toPrint = ''
        for col in range(board_size):
            if(col%3 == 0):
                toPrint += '|'
            toPrint += str(board[(row,col)])
        toPrint += '|'
        print(toPrint)
    print('-------------')


### to implement
def load_game(sudoku_file):
    state = {}
    with open(sudoku_file) as _file :
        for j , line in enumerate( _file.readlines()):
            for i , value in enumerate(line.rstrip("\n").split(",")):
                state[(j , i)] = int(value)
    return state
def check_board(board, x, *args):
    _i , _j = x

    def sudokuRange( _i , _j ):

        def triplerange( n ):
            yield from range( n -(n % 3) , n -(n % 3) + 3 )

        for i in triplerange(_i):
            for j in triplerange(_j):
                yield i , j

        for i in range(9):
            yield i , _j

        for j in range(9):
            yield _i , j

    for i , j in sudokuRange(_i , _j):
        if board[(i ,j)] == board[(_i , _j)] and (i , j) != (_i , _j ) :
            return False
    return True

def run_game(sudoku_file, print_mode = False):
    state = load_game( sudoku_file )
    if print_mode :
        print_board( state )

    ret = general_backtracking( [ key for key , value in state.items() if value == 0  ] , state  , 0 ,
                        range(1,10), check_board)
    if print_mode :
        print("~")
        print_board( state )

import os
if __name__ == "__main__":
    run_game( os.sys.argv[1] , True )
