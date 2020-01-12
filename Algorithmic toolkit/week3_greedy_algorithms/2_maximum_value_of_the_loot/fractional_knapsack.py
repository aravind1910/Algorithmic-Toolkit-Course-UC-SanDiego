# Uses python3
import sys

def get_optimal_value(n,capacity, weights, values):
    profit = 0.0
    frac=[]
    for i in range(n):
        frac.append(values[i]/weights[i])
    for i in range(len(frac)): 
        max_idx = i 
        for j in range(i+1, len(frac)): 
            if frac[max_idx] < frac[j]: 
                max_idx = j 
        frac[i], frac[max_idx] = frac[max_idx], frac[i]
        weights[i], weights[max_idx] = weights[max_idx], weights[i]
        values[i], values[max_idx] = values[max_idx], values[i]
    i=0
    profit=0
    while(weights[i]<=capacity ):
        capacity-=weights[i]
        profit+=values[i]
        i=i+1
        if(i==n):
            break
    if(i==n):
        return profit
    profit+=(capacity/weights[i])*values[i]
    return profit


if __name__ == "__main__":
    #data = list(map(int, sys.stdin.read().split()))
    #n, capacity = data[0:2]
    #values = data[2:(2 * n + 2):2]
    #weights = data[3:(2 * n + 2):2]
    values=[]
    weights=[]
    n,capacity=input().split()
    n,capacity=int(n),int(capacity)
    for i in range(n):
        a,b=input().split()
        values.append(int(a))
        weights.append(int(b))
    

    opt_value = get_optimal_value(n,capacity, weights, values)
    print("{:.4f}".format(opt_value))
