from collections import deque

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs(sx, sy):
    # 큐 생성
    q = deque()
    # 큐에 시작점, 카운트 집어넣기
    q.append((sx, sy, 0))
    # 방문 리스트
    visited = [[False] * C for _ in range(R)]
    # 시작점 방문처리
    visited[sx][sy] = True

    # 탐색 시작
    while q:
        # 현재 좌표, 카운트 확인
        x, y, cnt = q.popleft()

        # 다음 좌표 확인
        for dx, dy in dt:
            nx, ny = x+dx, y+dy

            # 범위 내인지
            if 0 <= nx < R and 0 <= ny < C:
                # 갈수 있는 곳인지
                pass


# 행의 개수 R, 열의 개수 C
R, C = map(int, input().split())
# 미로 maze
maze = [list(input()) for _ in range(R)]

# 지훈이 위치 찾기
for i in range(R):
    for j in range(C):
        # 재훈이 찾았다면,
        if maze[i][j] == 'J':
            # bfs 시작
            bfs(i, j)
            break