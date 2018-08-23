
def create_list():
    ret = input() 
    return list() if ret == "" else [ret] + create_list()
    
def contact_list(str_lst):
    ret = ""
    for _str in str_lst:
        ret += _str
    return ret

def average(num_list):    _sum = 0
    for _number in num_list :
        _sum += _number
    return _sum / len(num_list)

def cyclic(lst1 , lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return True
    if len(lst1) != len(lst2):
        return False

    def check_list(lst1 , lat2):
        for x , y in zip(lst1 , lst2):
            if x != y :
                return False
        return True

    for _ in range(len(lst2)):
        if check_list(lst1 , lst2) :
            return True
        else :
            lst2 = [lst2[-1]] + lst2[0:-1]
    return False
            
                
def histogram(n , num_list):
    ret = [ 0 for _ in range(n) ]
    for _number in num_list:
        ret[_number] += 1
    return ret 

import math 

def prime_factor(n):
    ret = []
    P = [ [] for _ in range(n+1) ]

    for i in range(4 ,n+1):
        for j in range(2 , i):
            if len(P[j]) == 0 and i % j == 0:
                p = j 
                while i % p == 0 :
                    P[i].append(j)
                    p *= p
          
    return P[n]

def cartesian(lst1 , lst2):
    ret = []
    for a in lst1:
        for b in lst2:
            ret.append((a,b))
    return ret

def paris(n , num_list):
    ret = []
    for i in range(len(num_list) - 1):
        for j in range (i + 1 , len(num_list)):
            if num_list[i] + num_list[j] == n :
                ret.append( (num_list[i], num_list[j]))
    return ret

def run():
    #print(create_list())
    #print(cyclic([1,2,3] , [2,3,1]))
    print(prime_factor(1324))