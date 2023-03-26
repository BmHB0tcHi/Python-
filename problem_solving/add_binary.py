
'''
    Given two binary strings a and b, return their sum as a binary string.
'''
def addBinary(a, b):
    return str(bin(int(a,2)+int(b,2)))[2:]