import sys
input = sys.stdin.readline

N = int(input().strip())
N_lst = list(map(int, input().strip().split()))

print(*sorted(list(set(N_lst))))