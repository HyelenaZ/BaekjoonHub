from collections import deque

N = int(input())
jump_size = list(map(int, input().split()))

visited = [-1] * N
q = deque()     
q.append((0, 0)) 
visited[0] = 0   # 시작 위치 점프 0으로 설정하기

while q:
    now_pos, jumps = q.popleft()
    
    max_jump = jump_size[now_pos] 
    
    for i in range(1, max_jump + 1):
        next_pos = now_pos + i 
        
        if next_pos < N and visited[next_pos] == -1:
            visited[next_pos] = jumps + 1 
            q.append((next_pos, jumps + 1)) 

print(visited[N-1]) 