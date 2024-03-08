dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def dfs(x, y, sec, sm):
    global fruit
    # 기저조건: 3초 지나면 종료
    if sec == 4:
        if fruit < sm:
            fruit = sm
        return

    # 재귀
    for _x, _y in dt:
        nx, ny = x + _x, y + _y

        if (0 <= nx < N) and (0 <= ny < N) and visited[nx][ny] == 0:
            # 방문처리
            visited[nx][ny] = 1
            dfs(nx, ny, sec+1, sm+trees[nx][ny])
            visited[nx][ny] = 0


# NxN크기의 격사, M명의 친구
N, M = map(int, input().split())
# 나무들 이차원리스트
trees = [list(map(int, input().split())) for _ in range(N)]

mx_fruit = 0
visited = [[0]*(N+1) for _ in range(N)]
for n in range(M):
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    fruit = 0

    visited[sx][sy] = 1
    dfs(sx, sy, 0, trees[sx][sy])
    visited[sx][sy] = 0
    mx_fruit += fruit

print(mx_fruit)