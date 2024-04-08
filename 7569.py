from collections import deque
import sys
input = sys.stdin.readline

# 판단
def judge():
    for i in range(N):
        for j in range(M):
            for h in range(H):
                if tomatos[i][j][h] == 0:
                    return 0
    else:
        return 1


# 6방향 (위, 아래, 왼, 오, 앞, 뒤) 델타값
dt = ((0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0))
# 3차원 bfs
def bfs(st_lst):
    # 큐 생성
    q = deque()
    # 큐에 시작점들 집어넣기
    q.extend(st_lst)

    cnt = 0

    # 탐색 시작
    while q:
        # 현재값 빼서 확인
        x, y, z, cnt = q.popleft()

        # 다음 좌표 탐색
        for dx, dy, dz in dt:
            nx, ny, nz = x + dx, y + dy, z + dz

            # 만약 범위 밖이라면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue

            # 다음 갈 좌표가 0이라면 방문 처리(1로 만들기) 후 큐에 넣기
            if tomatos[nx][ny][nz] == 0:
                tomatos[nx][ny][nz] = 1
                q.append((nx, ny, nz, cnt+1))
    # 찾았다면 cnt 리턴
    if judge():
        return cnt
    else:
        # 못찾았다면 -1 return
        return -1


# 상자의 크기 MxN, 높이 H
M, N, H = map(int, input().strip().split())
# 토마토 배열
temp = [list(map(int, input().strip().split())) for _ in range(N*H)]
tomatos = [[[] for _ in range(M)] for _ in range(N)]
# 3차원 배열 만들기
for i in range(N*H):
    for j in range(M):
        tomatos[i%N][j].append(temp[i][j])

# 시작점들 찾기 (1인 좌표들)
starts = []
for i in range(N):
    for j in range(M):
        for h in range(H):
            if tomatos[i][j][h] == 1:
                starts.append((i, j, h, 0))

print(bfs(starts))