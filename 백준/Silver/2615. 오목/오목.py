import sys
input = sys.stdin.readline 

board = [] 
for i in range(19):
    row = list(map(int, input().split()))
    board.append(row)
    
directions = {
    'right' : (0,1),    # 오른쪽 한 칸씩
    'down' : (1,0),     # 아래로 한 칸씩
    'diag_d' : (1,1),   # 오른쪽 아래로 한 칸씩
    'diag_u' : (-1,1)   # 오른쪽 위로 한 칸씩
}

winner = 0  # 아직 승자 없음
win_x = 0
win_y = 0

for y in range(19):
    for x in range(19):
        if board[x][y] != 0:
            current_stone = board[x][y]
            for dir, (dx,dy) in directions.items():
                stone_count = 1  # 현재 돌 포함해서 1부터 시작하기
                
                # ✅ 추가: 6개 이상의 연속된 돌 선택 방지를 위한 이전 방향 확인
                prev_x = x - dx
                prev_y = y - dy
                if 0 <= prev_x < 19 and 0 <= prev_y < 19 and board[prev_x][prev_y] == current_stone:
                    continue # 이전에 같은 돌이 있다면 건너뛰기(중간 돌은 제외하기)
                
                # 다음 위치 계산
                next_x = x + dx
                next_y = y + dy
                
                # 연속된 돌 세기
                while next_x >= 0 and next_x < 19 and next_y >= 0 and next_y < 19: 
                    if board[next_x][next_y] == current_stone: 
                        stone_count += 1
                        next_x += dx
                        next_y += dy
                    else:
                       break
                       
                if stone_count == 5:
	                # ✅ 추가: 6개 이상의 연속된 돌 선택 방지를 위한 이전 방향 확인
                    if next_x >= 0 and next_x < 19 and next_y >= 0 and next_y < 19 and board[next_x][next_y] == current_stone:
                        continue # 다음에 같은 돌이 있다면 6개의 돌들 가운데 중간돌임..
                    winner = current_stone
                    win_x = x+1
                    win_y = y+1
                    break  
                    
            if winner != 0:
                break  
        
        if winner != 0:
            break  
            
print(winner)
if winner != 0:
    print(win_x, win_y)