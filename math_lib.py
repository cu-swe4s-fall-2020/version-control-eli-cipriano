import math
def div(a, b):
    if b == 0:
        return -Inf
    else:
        return a/b

def sum(a, b):
    return print(a+b)

def prod(a, b):
    return a*b

def exp(a,b):
    return a**b

def sin(a, b):
    #b is either R or D, for radian or deg.
    if b.lower() == 'd':
        a = a/180*3.1415926

    
