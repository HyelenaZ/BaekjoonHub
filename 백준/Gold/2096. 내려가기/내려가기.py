import sys
input = sys.stdin.readline

# 1. 입력 받기
N = int(input()) 
now_line = list(map(int, input().split()))  # 현재 줄
max_now = now_line[:]  # 최대값 저장
min_now = now_line[:]  # 최소값 저장

# 2. 다음 줄부터
for i in range(N-1):
    next_line = list(map(int, input().split()))  # 다음 줄 입력
   
    # 현재 값 임시 저장
    max_before = max_now[:]  # 최대값 임시저장
    min_before = min_now[:]  # 최소값 임시저장
   
    # 왼쪽 칸(인덱스 0) - 위에서 올 수 있는 칸: before[0], before[1]
    max_now[0] = max(max_before[0], max_before[1]) + next_line[0]
    min_now[0] = min(min_before[0], min_before[1]) + next_line[0]
   
    # 가운데 칸(인덱스 1) - 위에서 올 수 있는 칸: before[0], before[1], before[2]
    max_now[1] = max(max_before[0], max_before[1], max_before[2]) + next_line[1]
    min_now[1] = min(min_before[0], min_before[1], min_before[2]) + next_line[1]
   
    # 오른쪽 칸(인덱스 2) - 위에서 올 수 있는 칸: before[1], before[2]
    max_now[2] = max(max_before[1], max_before[2]) + next_line[2]
    min_now[2] = min(min_before[1], min_before[2]) + next_line[2]

print(max(max_now), min(min_now))