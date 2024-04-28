import math
from gmpy2 import invert, powmod


def isPrime(Number):
    return 2 in [Number, 2**Number % Number]


def isOnCurve(x, y, a, b, p):
    return (x**3+a*x + b) % p == y**2 % p


def R(xp, yp, xq, yq, a, b, p):

    if xp == xq:
        s = ((3*xp**2+a)*invert(2*yp, p)) % p

    else:
        s = ((yp-yq)*invert(xp-xq, p)) % p

    xr = int((s**2 - xp - xq) % p)
    yr = int(-(yp - s*(xp-xr)) % p)

    return (xr, yr)


def main():

    p = int(input())
    a = int(input())
    b = int(input())
    xp = int(input())
    yp = int(input())
    xq = int(input())
    yq = int(input())
    if not isPrime(p):
        print("p is not prime")
        return
    if not isOnCurve(xp, yp, a, b, p):
        print("P is not on the curve")
        return
    if not isOnCurve(xq, yq, a, b, p):
        print("Q is not on the curve")
        return
    print(R(xp, yp, xq, yq, a, b, p))


if __name__ == "__main__":
    main()
