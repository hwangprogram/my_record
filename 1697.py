from collections import deque
def bfs(start):
    # 큐 생성
    q = deque()
    # 방문 배열 visited
    visited = [False] * 100001
    # 시작점, 카운트 큐에 넣기
    q.append((start, 0))
    # 시작점 방문처리
    visited[start] = True

    while q:
        # 큐에서 현재점 뽑기
        now, cnt = q.popleft()

        # 도착점 만난다면
        if now == X:
            return cnt

        for nxt in (now-1, now+1, 2*now):
            # nxt가 0과 100000사이라면
            if 0 <= nxt <= 100000:
                # 방문하지 않은 곳이라면
                if not visited[nxt]:
                    # 방문처리
                    visited[nxt] = True
                    # 큐에 넣기
                    q.append((nxt, cnt+1))
    return -1


# 수빈이 위치 N, 동생 위치 X
N, X = map(int, input().split())

# 넓이 우선 탐색(BFS) 실시 : 시작점 N, 도착점 X
print(bfs(N))