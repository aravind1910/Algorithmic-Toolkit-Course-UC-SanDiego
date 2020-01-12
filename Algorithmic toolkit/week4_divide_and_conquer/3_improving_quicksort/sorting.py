# Uses python3
import sys
import random

def partition3(a, l, r):
    




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quicksort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
