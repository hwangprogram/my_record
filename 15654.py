path = []
def dfs(cnt):
    # 기저조건: cnt가 M이되면 종료
    if cnt == M:
        print(*path)
        return

    # 재귀조건: nums에서 요소를 뽑는가 뽑지 않는가
    for i in range(N):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(cnt+1)
            path.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

dfs(0)