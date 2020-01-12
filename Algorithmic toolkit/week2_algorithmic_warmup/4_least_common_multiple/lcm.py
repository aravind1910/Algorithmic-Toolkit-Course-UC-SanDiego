# Uses python3
import sys
def gcd_naive(a, b):
    if (b != 0):
       return gcd_naive(b, a%b);
    else:
       return a;


def lcm_naive(a, b):
    return (a*b)//gcd_naive(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

