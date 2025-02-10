import sys
input = sys.stdin.readline

N = int(input())

max_dp = list(map(int, input().split()))
min_dp = max_dp[:]

for _ in range(N-1):
    current = list(map(int, input().split()))
    prev_max = max_dp[:]
    prev_min = min_dp[:]
    
    max_dp[0] = max(prev_max[0], prev_max[1]) + current[0]
    max_dp[1] = max(prev_max[0], prev_max[1], prev_max[2]) + current[1]
    max_dp[2] = max(prev_max[1], prev_max[2]) + current[2]
    
    min_dp[0] = min(prev_min[0], prev_min[1]) + current[0]
    min_dp[1] = min(prev_min[0], prev_min[1], prev_min[2]) + current[1]
    min_dp[2] = min(prev_min[1], prev_min[2]) + current[2]

print(max(max_dp), min(min_dp))