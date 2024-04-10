# 델타값: 0 북, 1동, 2 남, 3 서
dt = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 방의 크기 NxM
N, M = map(int, input().split())
# 로봇청소기 좌표 r,c, 방향 dr
r, c, dr = map(int, input().split())
# 방 청소상태 room
room = [list(map(int, input().split())) for _ in range(N)]
# 방문 리스트
visited = [[0] * M for _ in range(N)]

# 시작점 방문처리, 카운트
visited[r][c] = 1
cnt = 1

# 시뮬레이션 시작
while True:
    # 청소 여부
    clean = False

    # 4방향 탐색 (반시계 방향)
    for _ in range(4):
        dr = (dr+3)%4
        nr, nc = r + dt[dr][0], c + dt[dr][1]

        # 범위 내이며, 청소할 수 있는 칸이라면
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            # 방문하지 않은 곳이라면
            if visited[nr][nc] == 0:
                # 방문처리
                visited[nr][nc] = 1
                # 청소 카운트
                cnt += 1
                # 해당 위치로 이동
                r, c = nr, nc
                # 청소 했음을 표시
                clean = True
                break

    # 청소할 곳이 없어 하지 못했다면
    if not clean:
        # 후진할 수 없는 곳이라면 break
        if room[r-dt[dr][0]][c-dt[dr][1]] == 1:
            print(cnt)
            break
        # 후진할 수 있는 곳이라면 후진
        else:
            r, c = r - dt[dr][0], c - dt[dr][1]