import sys
input = sys.stdin.readline

def fib(n):
    global cnt1

    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibo(n):
    global cnt2

    f[1] = f[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-2] + f[i-1]
    return f[n]


N = int(input())
f = [0]*(N+1)
cnt1, cnt2 = 0, 0

fib(N)
fibo(N)
print(cnt1, cnt2)