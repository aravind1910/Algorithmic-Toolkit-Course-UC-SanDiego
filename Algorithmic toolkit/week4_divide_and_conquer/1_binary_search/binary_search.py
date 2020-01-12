# Uses python3
import sys

def binary_search (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, l, mid-1, x) 
        else: 
            return binary_search(arr, mid + 1, r, x) 
    else: 
        return -1
if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #m = data[n + 1]
    #a = data[1 : n + 1]
    l=[int(i) for i in input().split()]
    a=l[1:]
    l=[int(i) for i in input().split()]
    n=l[1:]
    
    #for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
    for x in n:
        print(binary_search(a,0,len(a)-1, x), end = ' ')
