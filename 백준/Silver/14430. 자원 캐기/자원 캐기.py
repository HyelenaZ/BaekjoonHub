N, M = map(int, input().rstrip().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().rstrip().split())))

# DP 배열 (자원의 최대 개수 저장)
dp = [[0] * M for _ in range(N)]

# (0,0) 위치 초기화
dp[0][0] = grid[0][0]

# 첫 행 초기화
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# 첫 열 초기화
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + grid[i][0]

# 나머지 칸 채우기
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[N-1][M-1])