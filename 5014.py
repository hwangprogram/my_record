from collections import deque
import sys
input = sys.stdin.readline

# 너비우선 탐색
def bfs(start):
    # 큐 만들기
    q = deque()
    # 방문 배열 만들기 : 최대 높이인 F만큼
    visited = [False] * (F+1)
    # 큐에 시작점, 카운트 넣기
    q.append((start, 0))
    # 시작점 방문처리
    visited[start] = True

    # 탐색 시작
    while q:
        # 현위치, 거리 꺼내기
        pos, dist = q.popleft()

        # 만약, 도착점에 도달했다면
        if pos == G:
            # 지금까지의 거리 반환
            return dist

        # 위로 가거나, 밑으로 가거나
        for to in (pos + U, pos - D):
            # to가 0보다 크거나 같고, F보다 작거나 같을 때
            if 0 < to <= F:
                # 방문하지 않았다면
                if not visited[to]:
                    # 방문처리
                    visited[to] = True
                    # 큐에 넣기
                    q.append((to, dist+1))
    # 찾지 못했다면
    return 'use the stairs'


# 건물 층수 F, 시작 층 S, 도착 층 G, 올라갈 수 있는 값 U, 내려갈 수 있는 값 D
F, S, G, U, D = map(int, input().strip().split())

# S부터 너비우선탐색(BFS) 시작
ans = bfs(S)
print(ans)