from collections import deque

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs(sx, sy):
    # 큐 생성
    q = deque()
    # 큐에 시작점 넣기
    q.append((sx, sy))
    # 시작점 방문처리
    visited[sx][sy] = True

    # 탐색
    while q:
        # 현재 좌표
        x, y = q.popleft()

        # 다음 좌표
        for dx, dy in dt:
            nx, ny = x + dx, y + dy

            # 범위 확인
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않은 곳이며, 갈 수 있는 곳이라면
                if not visited[nx][ny] and cabs[nx][ny] == 1:
                    # 방문처리
                    visited[nx][ny] = True
                    # 큐에 넣기
                    q.append((nx, ny))


T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    cabs = [[0] * M for _ in range(N)]
    for k in range(K):
        cy, cx = map(int, input().split())
        cabs[cx][cy] = 1

    # 방문 배열
    visited = [[False] * M for _ in range(N)]
    # 필요한 배추흰지렁이
    need_bugs = 0

    for i in range(N):
        for j in range(M):
            if cabs[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                need_bugs += 1

    print(need_bugs)