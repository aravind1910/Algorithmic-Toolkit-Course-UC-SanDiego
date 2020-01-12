# Uses python3
import sys
import math as m
def optimal_summands(n):
    summands = []
    x=m.floor((-1+m.sqrt(1+8*n))/2)
    summands=[i for i in range(1,x)]
    summands.append(n-(x*(x-1)//2))
    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
