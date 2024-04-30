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
    yr = int((s*(xp-xr) - yp) % p)

    return (xr, yr)


def exchange(p, a, b, xg, yg, x, y):
    x1 = xg
    y1 = yg
    times = x*y
    # while times/2 > 0:
    #     x1, y1 = R(x1, y1, x1, y1, a, b, p)
    for i in range(x-1):
        x1, y1 = R(x1, y1, xg, yg, a, b, p)

    x2 = x1
    y2 = y1

    for j in range(y-1):
        x2, y2 = R(x2, y2, x1, y1, a, b, p)

    return (x2, y2)


def main():

    p = int(input())
    a = int(input())
    b = int(input())
    xg = int(input())
    yg = int(input())
    x = int(input())
    y = int(input())

    if not isPrime(p):
        print("p is not prime")
        return
    if not isOnCurve(xg, yg, a, b, p):
        print("P is not on the curve")
        return

    xr, yr = exchange(p, a, b, xg, yg, x, y)
    print(str(xr)+str(yr))


if __name__ == "__main__":
    main()
