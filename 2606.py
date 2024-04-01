def dfs(start):
    global cnt

    # 시작점 방문처리
    visited[start] = True

    # 재귀조건: 인접 노드 확인
    for node in adjl[start]:
        # 방문하지 않았다면
        if not visited[node]:
            # 방문 처리
            visited[node]
            # 카운트
            cnt += 1
            # 탐색
            dfs(node)

# 노드 수 V
V = int(input())
# 간선 수 E
E = int(input())

# 인접리스트 adjl
adjl = [[] for _ in range(V+1)]
# 간선 정보 저장
for _ in range(E):
    s, e = map(int, input().split())
    adjl[s].append(e)
    adjl[e].append(s)

# 방문 리스트 visited
visited = [False] * (V+1)
# 카운트
cnt = 0
# 깊이 우선 탐색 DFS
dfs(1)
print(cnt)