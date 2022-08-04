from math import gcd
from random import randint

def primitive(p):
    roots=[]
    coprimes = set(i for i in range(1,p) if gcd(i,p)==1)
    for g in range(1,p):
        actual = set(pow(g,i,p) for i in range(1, p))
        if(coprimes == actual):
            roots.append(g)
    return min(roots)
if __name__ == "__main__":
    p = int(input("Prime: "))
    x = primitive(p)
    print("Primitive Root = ",x)
    xa = randint(1,15)
    print("Random Private Key A = ",xa)
    ya = pow(x,xa,p)
    xb = randint(1,15)
    print("Random Private Key B = ",xa)
    yb = pow(x,xb,p)
    print("Public Key A = ",ya)
    print("Public Key B = ",yb)
    k = pow(yb,xa,p)
    print("Shared Key = ",k)
