import math

def period(L,g):
    
    x = isinstance(L,(float,int))
    if x == False:
        print('Wrong data type for L, please enter a number and try again.')
    
    y = isinstance(g,(float,int))
    if y == False:
        print('Wrong data type for g, please enter a number and try again.')
    
    T = 2*3.14*math.sqrt(L/g)
    
    return T

period(5,9.81)