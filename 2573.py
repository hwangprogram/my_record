'''
1. 1년마다 각 칸의 얼음이 줄어든다
    -> 자신의 동 서 남 북 에 있는 0값의 개수만큼
2. 그 때마다 빙산의 개수를 센다
    -> bfs 활용
'''
from collections import deque

# 델타값
dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
# bfs
def bfs(sx, sy):
    # 큐 생성
    q = deque()
    # 큐에 시작점 집어넣기
    q.append((sx, sy))
    # 시작점 방문처리
    visited[sx][sy] = True

    # 탐색 시작
    while q:
        # 현재 위치
        x, y = q.popleft()

        # 다음 좌표 확인
        for dx, dy in dt:
            nx, ny = x + dx, y + dy

            # 범위 내인지
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았으며, 0이 아니라면
                if not visited[nx][ny] and ices[nx][ny] != 0:
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐애 넣기
                    q.append((nx, ny))


# NxM 크기의 배열
N, M = map(int, input().split())
# 얼음들 배치 ices
ices = [list(map(int, input().split())) for _ in range(N)]

# 년
year = 0

# 2차원 배열 순회하며 얼음 줄여주기
while True:
    # 방문 리스트
    visited = [[False]*M for _ in range(N)]

    # 섬 갯수 세기
    island_count = 0
    # 0이 아닌 값에 대해 bfs 진행
    for i in range(N):
        for j in range(M):
            # 방문하지 않은 곳이며, 0이 아니라면
            if not visited[i][j] and ices[i][j] != 0:
                # 섬 카운트 +1
                island_count += 1
                bfs(i, j)
    # 섬 카운트가 2 이상이면
    if island_count >= 2:
        # while문 탈출
        break

    # 빙산 줄이기를 위한 방문 리스트
    visited2 = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ices[i][j] != 0:
                # 방문처리 (원래 섬이 있던 자리가 0이 되었을 때 세지 않도록)
                visited2[i][j] = True
                zero_cnt = 0

                for di, dj in dt:
                    ni, nj = i + di, j + dj

                    # 범위 내
                    if 0 <= ni < N and 0 <= nj < M:
                        # 0(zero)이고, 방문하지 않았다면
                        if ices[ni][nj] == 0 and not visited2[ni][nj]:
                            zero_cnt += 1

                if ices[i][j] - zero_cnt < 0:
                    ices[i][j] = 0
                else:
                    ices[i][j] -= zero_cnt

    # 전부 0이라면 빠져나와야 함
    total = 0
    for i in range(N):
        total += sum(ices[i])
        if total > 0:
            break

    if total == 0:
        year = 0
        break

    # 1년 경과
    year += 1

# 몇 년 걸렸는지 출력
print(year)
