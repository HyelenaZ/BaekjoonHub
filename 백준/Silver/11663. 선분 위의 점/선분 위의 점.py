import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(M):
    start, end = map(int, input().split())
   
    start_position = N
    left, right = 0, N-1
    
    while left <= right:
        mid = (left+right) //2
        if points[mid] >= start:
            start_position = mid
            right = mid-1
        else:
            left = mid+1
            
    end_position = -1
    left, right = 0, N-1
    
    while left <= right:
        mid = (left+right) //2
        if points[mid] <= end:
            end_position = mid
            left = mid+1
        else:
            right = mid-1
        
    if end_position >= start_position:
        print(end_position - start_position + 1)
    else:
        print(0)