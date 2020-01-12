# Uses python3
import sys
f = [0] * 61;
f[0] = 0; 
f[1] = 1; 
for i in range(2, 61):
    f[i] = (f[i - 1] + f[i - 2]) % 10; 

def get_fibonacci_last_digit_naive(n):
    return f[n % 60]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
