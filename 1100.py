chess = [list(input()) for _ in range(8)]

cnt = 0
for i in range(8):
    for j in range(8):
        # 홀수 줄
        if i % 2 == 0 and j % 2 == 0 and chess[i][j] == 'F':
            cnt += 1
        # 짝수 줄
        if i % 2 == 1 and j % 2 == 1 and chess[i][j] == 'F':
            cnt += 1

print(cnt)