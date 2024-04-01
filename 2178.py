from collections import deque

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
# 넓이 우선 탐색 bfs
def bfs(sx, sy):
    # 큐 생성
    q = deque()
    # 방문 리스트 생성
    visited = [[False] * M for _ in range(N)]
    # 시작 정점 방문 처리
    visited[sx][sy] = True
    # 시작 정점, 카운트 큐에 넣기
    q.append((sx, sy, 1))

    # 탐색 시작
    while q:
        # 좌표, 카운트 빼내고
        x, y, cnt = q.popleft()

        # 목적지 도착하면 cnt값 출력하고 stop
        if x == N-1 and y == M-1:
            print(cnt)
            break
        # 다음 좌표 찾기
        for dx, dy in dt:
            nx, ny = x + dx, y + dy

            # 범위 내라면,
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았으며, 갈 수 있는 곳이라면,
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    # 방문처리
                    visited[nx][ny] = True
                    # 다음 좌표, 카운트+1 큐에 넣기
                    q.append((nx, ny, cnt+1))
    return


# N x M 크기의 배열
N, M = map(int, input().split())

# 배열 arr
arr = [list(map(int, input())) for _ in range(N)]

bfs(0, 0)