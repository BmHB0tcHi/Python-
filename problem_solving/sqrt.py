'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
    The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''
def mySqrt(x):
    if (x == 1):
        return 1
    for n in range(1, x+1):
        n_square = n*n
        if (n_square == x):
            return n
        if (x - n_square) < 0:
            return n-1

     
print(mySqrt(25))
print (mySqrt(16))
print (mySqrt(15))
print (mySqrt(300))
