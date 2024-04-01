'''
백준 2644 촌수계산

촌수: N1으로부터 N2까지의 거리
'''
from collections import deque
def bfs(start):
    # 큐 생성
    q = deque()
    # 방문 배열 생성
    visited = [False] * (N+1)

    # 큐에 시작점, 카운트 넣기
    q.append((start, 0))
    # 시작점 방문처리
    visited[start] = True
    # 탐색
    while q:
        # 현재 노드 꺼내서 확인
        now, cnt = q.popleft()

        # 도착점 만나면 종료
        if now == N2:
            # 지금까지 카운트값 반환
            return cnt

        # 현재 노드의 인접노드 확인
        for nxt in adjl[now]:
            # 만약, 방문한 곳이면 continue
            if visited[nxt]:
                continue

            # 방문하지 않았다면
            # 큐에 삽입
            q.append((nxt, cnt+1))
            # 방문처리
            visited[nxt] = True
    # 찾지 못했다면(관계 X) -1 반환
    return -1


# 노드 수 N
N = int(input())
# 촌수 구할 두 사람의 노드 번호
N1, N2 = map(int, input().split())
# 간선 수 E
E = int(input())
# 인접 리스트 adjl
adjl = [[] for _ in range(N+1)]
# 1~E 간선 정보
for _ in range(E):
    s, e = map(int, input().split())
    adjl[s].append(e)
    adjl[e].append(s)

# N1출발, N2도착으로 하여 BFS탐색
print(bfs(N1))