import sys
input = sys.stdin.readline

N, K = map(int, input().split()) 
bottles = []
for _ in range(N):
    bottles.append(int(input()))

start = 1
end = max(bottles)
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    # 이 양으로 몇 명에게 줄 수 있는지 계산
    total_people = 0
    for bottle in bottles:
        total_people += bottle // mid
    
    if total_people >= K:
        answer = mid 
        start = mid + 1 
    else:
        end = mid - 1
        
print(answer)