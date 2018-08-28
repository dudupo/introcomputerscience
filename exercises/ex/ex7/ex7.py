from copy import deepcopy as copy

def print_to_n(n):
    if n > 1 :
        print_to_n(n-1)
    print(n)

def print_reversed(n):
    print(n)
    if n > 1 :
        print_reversed(n-1)


def gcd(a ,b):
    return a if b == 0 else gcd(b , a %b )

def is_prime(n):

    def f(n , i):
        return ((gcd(n, i) > 1) or f(n , i- 1)) if i > 1 else False

    return f( n  , int(n ** 0.5))

def divisor(n):
    def divisor(n , i):
        if i == 0 :
            return []
        ret = divisor (n , i - 1)
        if n % i == 0 :
            ret.append(i)
        return ret
    return divisor( n , n )

def factorial(n):
    return 1  if n == 1 else n * factorial(n-1)
def exp_x_n(n , x):
    return 1 if n == 0 else (x ** n / factorial(n)) + exp_x_n(n-1 , x)


def print_binary_sequences(n):

    def binary_sequences(n):

        if n == 0 :
            return [ "" ]

        ret = []
        for seq in binary_sequences(n-1):
            ret.append("0" + seq)
            ret.append("1" + seq)
        return ret

    for seq in binary_sequences(n):
        print(seq)

def print_sequences(char_list, n):

    def char_sequences(char_list , n):

        if n == 0 :
            return [ "" ]

        ret = []
        for seq in char_sequences(char_list , n-1):
            for _char in char_list :
                ret.append( _char + seq  )
        return ret

    for seq in char_sequences(char_list , n):
        print(seq)


def no_repetition_sequences(char_list ,n):

    if n == 0 :
        return  [ (copy(char_list), "") ]

    ret = []
    for retchar_list , seq in no_repetition_sequences(char_list , n-1):
        for _char in retchar_list :
            l = copy(retchar_list)
            l.remove( _char )
            ret.append( ( l , _char + seq ) )
    return ret

def print_no_repetition_sequences(char_list, n):
    for retchar_list ,seq in no_repetition_sequences(char_list ,n):
        print(seq)

def no_repetition_sequences_list(char_list, n):
    return [seq for retchar_list , seq in no_repetition_sequences(char_list ,n)]


def play_hanoi(hanoi, n, src, dest, temp):
    if (n  == 1):
        hanoi.move(src , dest)
        return

    play_hanoi(hanoi, n -1 , src , temp, dest)
    hanoi.move(src , dest)
    play_hanoi(hanoi, n-1 , temp , dest , src)

if __name__ == "__main__" :
    print_no_repetition_sequences(['a' , 'b' , 'c' , 'd'] , 4)
    print(divisor(15))
    print(exp_x_n(12 , 0.5))
