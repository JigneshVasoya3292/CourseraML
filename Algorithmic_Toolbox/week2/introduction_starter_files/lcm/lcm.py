# Uses python3
import sys

def lcm_naive(a, b):
    gcdab = gcd(a,b)
    # a and b could be 2*10^9 each
    return (a*b)//gcdab


def gcd(a,b):
    if b <=0:
        return a

    return gcd(b, a%b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

