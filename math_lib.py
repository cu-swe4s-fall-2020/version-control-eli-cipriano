def div(a, b):
    if b == 0:
        return -Inf
    else:
        return a/b


def sum(a, b):
    return a+b


def prod(a, b):
    return a*b


def exp(a, b):
    return a**b


def sin(a, b):
    # b is either R or D, for radian or deg.
    if b.lower() == 'd':
        sd = a/180*3.1415926
    sd = sd - sd**3/(6) + sd**5/(120) - sd**7/(5040) + sd**9/(362880)
    return sd
