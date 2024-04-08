import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_lst = [0]
N_lst.extend(list(map(int, input().split())))

for n in range(1, N+1):
    N_lst[n] += N_lst[n-1]


for _ in range(M):
    i, j = map(int, input().split())

    print(N_lst[j]-N_lst[i-1])