dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def dfs(x, y):
    global cnt

    # 방문처리
    aparts[x][y] = 0
    # 세기
    cnt += 1

    # 재귀조건: 좌표탐색(델타)
    for dx, dy in dt:
        nx, ny = x + dx, y + dy

        # 범위 내이며, 이동할 수 있는 곳이라면
        if 0 <= nx < N and 0 <= ny < N and aparts[nx][ny] == 1:
            dfs(nx, ny)


N = int(input())
aparts = [list(map(int, input())) for _ in range(N)]

# 단지 인원 계산 리스트
comp = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if aparts[i][j] == 1:
            dfs(i, j)
            comp.append(cnt)

# 오름차순 정렬
comp.sort()
print(len(comp))
for val in comp:
    print(val)