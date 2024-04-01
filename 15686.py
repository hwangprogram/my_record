import sys
input = sys.stdin.readline

# 치킨집에서 M개 뽑기
remain = []
def dfs(idx):
    # 최소 거리값
    global mn_dist

    # 기저조건: remain의 길이가 M이 되면 종료
    if len(remain) == M:
        # 정답처리: 각 집에서 이 두 치킨집까지의 거리계산
        dist = chicken_dist(remain)
        mn_dist = min(dist, mn_dist)
        return

    # 재귀조건: 치킨집 좌표를 추가할 것인가, 말 것인가
    for i in range(idx, len(chicken_res)):
        res = chicken_res[i]
        remain.append(res)
        dfs(i+1)
        remain.pop()

def chicken_dist(restaurant):
    final_dist = 0

    for house in houses:
        # 각 집별 최소값을 구해야 함
        mn_house = float('inf')
        for res in restaurant:
            dist = abs(house[0] - res[0]) + abs(house[1] - res[1])
            mn_house = min(dist, mn_house)
        final_dist += mn_house

    return final_dist


N, M = map(int, input().strip().split())
chicken = [list(map(int, input().strip().split())) for _ in range(N)]

# 집, 치킨집 찾기
houses = []
chicken_res = []
for i in range(N):
    for j in range(N):
        if chicken[i][j] == 1:
            houses.append((i, j))
        elif chicken[i][j] == 2:
            chicken_res.append((i, j))

mn_dist = float('inf')
dfs(0)
print(mn_dist)