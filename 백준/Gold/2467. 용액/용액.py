import sys
input = sys.stdin.readline
N = int(input())  # inpur -> input 오타 수정
liquids = list(map(int, input().split()))
min_gap = float('inf')  # zero_gap -> min_gap으로 통일
result = []

for i in range(N-1):
    fixed_left = liquids[i]
    
    left = i+1
    right = N - 1
    
    while left <= right:
        mid = (left + right) // 2
        # 두 용액 혼합값
        mixed_value = fixed_left + liquids[mid]
        
        if abs(mixed_value) < min_gap: 
            min_gap = abs(mixed_value)
            result = [fixed_left, liquids[mid]]
            
        if mixed_value < 0:
            left = mid + 1
        else:
            right = mid - 1

print(result[0], result[1])