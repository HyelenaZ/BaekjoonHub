from collections import deque

N = int(input())
color_lst= []  

for _ in range(N):
    row = list(input().strip()) 
    color_lst.append(row)

def count_area(x, y, color, visited, is_colorblind=False):
    # 상하좌우 이동 방향
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        now_x, now_y = queue.popleft()
        
        # 상하좌우 탐색
        for move_x, move_y in moves:
            next_x = now_x + move_x
            next_y = now_y + move_y
            
            # 그리드 범위를 벗어나면 스킵
            if not (0 <= next_x < N and 0 <= next_y < N):
                continue
            
            if visited[next_x][next_y]:
                continue
            
            next_color = color_lst[next_x][next_y]
            
            if not is_colorblind and next_color == color:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y))
            
            elif is_colorblind:
                if (color in 'RG' and next_color in 'RG') or (color == 'B' and next_color == 'B'):
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

def count_total_areas(is_colorblind):
    visited = [[False] * N for _ in range(N)]
    area_count = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count_area(i, j, color_lst[i][j], visited, is_colorblind)
                area_count += 1
    
    return area_count

normal_count = count_total_areas(False)    
colorblind_count = count_total_areas(True) 

print(normal_count, colorblind_count)