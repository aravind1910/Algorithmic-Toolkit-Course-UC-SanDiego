# python3
import sys
def compute_min_refills(distance, tank,n, stops):
    stop=0
    stops=[0]+stops+[distance]
    count=0
    while(True):
        i=stop
        if(stops[stop+1]-stops[stop]>tank):
            return -1
        if(distance-stops[stop]<=tank):
            return count
        while(i<n-1 and stops[i+1]-stops[stop]<=tank):
            i=i+1
        stop=i
        count=count+1
    return count

if __name__ == '__main__':
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    d=int(input())
    m=int(input())
    n=int(input())
    stops=[int(i) for i in input().split()]
    print(compute_min_refills(d, m, n+2, stops))
