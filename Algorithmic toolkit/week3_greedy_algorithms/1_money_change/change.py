# Uses python3
import sys

def get_change(m):
    count1,count2,count3=0,0,0
    count1=m//10
    m-=10*count1
    count2+=m//5
    m-=5*count2
    count3+=m
    return count1+count2+count3

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
