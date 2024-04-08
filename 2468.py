from collections import deque
import sys
input = sys.stdin.readline

def decreasing(n, arr):
    for i in range(N):
        for j in range(N):
            arr[i][j] -= n
            if arr[i][j] < 0:
                arr[i][j] = 0


dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def search(arr):
    global count

    # for문 순회하며 0이 아닌 값 찾기
    for i in range(N):
        for j in range(N):
            # 0이 아니며, 방문하지 않았다면 탐색 시작
            if arr[i][j] != 0 and not visited[i][j]:
                # 영역 카운트
                count += 1

                # 큐 선언
                q = deque()
                # 큐에 시작점 넣기
                q.append((i, j))
                # 방문처리
                visited[i][j] = True

                # 탐색
                while q:
                    # 현위치 확인
                    x, y = q.popleft()

                    # 다음 좌표 탐색
                    for dx, dy in dt:
                        # 다음 좌표
                        nx, ny = x + dx, y + dy

                        # 범위 내라면
                        if 0 <= nx < N and 0 <= ny < N:
                            # 방문하지 않은 곳이며, 0이 아니라면,
                            if not visited[nx][ny] and arr[nx][ny] != 0:
                                # 방문처리
                                visited[nx][ny] = True
                                # 큐에 넣기
                                q.append((nx, ny))


N = int(input().strip())
heights = [list(map(int, input().strip().split())) for _ in range(N)]

# 최대값 뽑기
max_val = 0
for i in range(N):
    val = max(heights[i])
    max_val = max(val, max_val)

# 순회하면서 높이 줄여주기
# 각 영역 세어주기
# 최대 영역 수
max_count = 0
for i in range(max_val):
    # 영역 수
    count = 0
    # 방문 배열
    visited = [[False] * N for _ in range(N)]
    og_heights = [row[:] for row in heights]
    decreasing(i, heights)
    search(heights)
    max_count = max(max_count, count)
    heights = [row[:] for row in og_heights]

print(max_count)