from collections import deque
import sys
input = sys.stdin.readline

def dfs(n):
    # 현재 방문한 정점을 출력
    print(n, end=' ')
    # 방문처리
    visited[n] = True

    # n번 노드의 인접 정점을 방문(깊이우선)
    for node in adjl[n]:
        # 방문하지 않았다면
        if not visited[node]:
            # 재귀호출
            dfs(node)


def bfs(n):
    # 큐 생성
    q = deque()

    # 방문 리스트 초기화
    visited = [False] * (N+1)

    # 시작점 큐에 넣기
    q.append(n)
    # 방문처리
    visited[n] = True

    # 큐가 빌 때까지 반복
    while q:
        # 출발점
        start = q.popleft()

        # 방문한 정점 print
        print(start, end=' ')

        # 인접 정점들에 대해
        for node in adjl[start]:
            # 방문하지 않았다면
            if not visited[node]:
                # 큐에 다음 정점 넣음
                q.append(node)
                # 방문처리
                visited[node] = True


# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

# 인접 리스트 adjl
adjl = [[] * (N+1) for _ in range(N+1)]

# 방문 정보 visited
visited = [False] * (N+1)

# 각 간선들의 연결정보
for _ in range(M):

    n1, n2 = map(int, input().split())
    # 인접 리스트 생성 작은 노드부터
    adjl[n1].append(n2)
    adjl[n2].append(n1)

# 인접 리스트 정렬
for a in adjl:
    a.sort()

# 깊이 우선 탐색 dfs
dfs(V)
print()
# 넓이 우선 탐색 bfs
bfs(V)