import sys
input = sys.stdin.readline

N = int(input())
house_cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

dp[0][0] = house_cost[0][0]
dp[0][1] = house_cost[0][1]
dp[0][2] = house_cost[0][2]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house_cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house_cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house_cost[i][2]
    
min_cost = min(dp[N-1])
print(min_cost)