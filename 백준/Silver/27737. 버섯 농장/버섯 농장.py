from collections import deque

N, M, K = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

def find_connected(x, y, visited):
    count = 1 
    queue = deque([(x, y)])
    visited[x][y] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

visited = [[False]*N for _ in range(N)]
groups = []
total_zeros = 0 

for i in range(N):
    for j in range(N):
        if board[i][j] == 0 and not visited[i][j]:
            group_size = find_connected(i, j, visited)
            groups.append(group_size)
            total_zeros += group_size

if total_zeros == 0 or M == 0:
    print("IMPOSSIBLE")
else:
    total_needed = 0
    for size in groups:
        needed = (size + K - 1) // K
        total_needed += needed
    
    if total_needed <= M:
        print("POSSIBLE")
        print(M - total_needed)
    else:
        print("IMPOSSIBLE")