# Uses python3
import sys
import itertools

def partition(a,p,r):
    pivot = p
    for i in range(p+1,r+1):
        if(a[i]<a[pivot]):
            tmp = a[i]
            a[i] = a[pivot+1]
            a[pivot+1] = a[pivot]
            a[pivot] = tmp
            pivot = pivot + 1
    return pivot

def quickSort(a,p,r):
    if(r>p):
        q = partition(a, p, r)
        quickSort(a,p,q-1)
        quickSort(a,q+1,r)


def partition3(A):
    if(sum(A) % 3 == 0):
        quickSort(A,0,len(A) - 1)
        sums = [[],[],[]]
        i = len(A) - 1
        while(i > - 1):
            k = 0
            pacted = False
            while(not pacted and k < len(sums)):
                if(sum(sums[k]) + A[i] <= sum(A)//3):
                    sums[k].append(A[i])
                    pacted = True
                k+=1
            i -=1
        return int(sum(sums[0]) == sum(sums[1]) == sum(sums[2]) == sum(A)//3)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

