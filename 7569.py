# 6방향 (위, 아래, 왼, 오, 앞, 뒤) 델타값
dt = ((0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0))
# 3차원 탐색 시작
def dim_3_find():
    pass


# 상자의 크기 MxN, 높이 H
M, N, H = map(int, input().split())
# 토마토 배열
temp = [list(map(int, input().split())) for _ in range(N*H)]
tomatos = [[[] for _ in range(M)] for _ in range(N)]
# 3차원 배열 만들기
for i in range(N*H):
    for j in range(M):
        tomatos[i%N][j].append(temp[i][j])

print(tomatos)