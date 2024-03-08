'''
Softeer 연탄의 크기

각 집의 난로의 크기가 주어진다.
난로의 반지름의 길이가 연탄의 반지름의 길이의 배수인 집에서만 사용가능하다
난방을 최대로 받을 수 있는 집 수를 구하라
'''

import sys

N = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))

mx_cnt = 0

for i in range(2, max(house)+1):
    cnt = 0
    for h in house:
        if h % i == 0:
            cnt += 1
    if cnt > mx_cnt:
        mx_cnt = cnt

print(mx_cnt)