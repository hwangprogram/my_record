import sys
input = sys.stdin.readline

def find_set(x):
    # 기저조건: 부모 == 나 라면 나를 return
    if x == parent[x]:
        return x

    return find_set(parent[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 작은 부모로 union
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


V, E = map(int, input().strip().split())
V += 1
parent = list(range(V))
# 간선 정보 저장
edges = []
for _ in range(E):
    s, e, w = map(int, input().strip().split())
    edges.append([s, e, w])
# 가중치 기준으로 정렬
edges.sort(key=lambda x: x[2])

sum_weight = 0
cnt = 0

# 간선들 모두 확인
for s, e, w in edges:
    # 사이클이 발생하면 pass
    if find_set(s) == find_set(e):
        continue

    cnt += 1

    # 싸이클이 없다면 방문처리
    union(s, e)
    sum_weight += w

    # MST 완성 -> 간선의 개수가 V-1개일 때
    if cnt == V-1:
        break

print(sum_weight)