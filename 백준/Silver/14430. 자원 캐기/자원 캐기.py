N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# DP 배열 (자원의 최대값 저장)
dp = [[0] * M for _ in range(N)]
dp[0][0] = grid[0][0]

# 첫 행 
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + grid[0][j]
# 첫 열
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + grid[i][0]
# 나머지 칸 계산
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[N-1][M-1])