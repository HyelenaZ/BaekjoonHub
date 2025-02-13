board = [] 
for i in range(19):
    row = list(map(int, input().split()))
    board.append(row)

directions = {
    'right' : (0,1),  # 오른쪽 한 칸씩
    'down' : (1,0),  # 아래로 한 칸씩
    'diag_d' : (1,1), # 오른쪽 아래로 한 칸씩
    'diag_u' : (-1,1)   # 오른쪽 위로 한 칸씩
}

winner = 0 # 아직 승자 없음
win_x = 0
win_y = 0

for y in range(19):
    for x in range(19):
        if board[x][y] != 0:
            current_stone = board[x][y]

            for dir, (dx,dy) in directions.items():
                stone_count = 1  # 현재 돌 포함해서 1부터 시작하기

                ## !@##$@#$@# *** 시작점 앞단의 방향에서 온 돌과 색깔 확인 체크 **** 
                ## 아래에 시작점 기준으로 5목인 순간 더이상 탐색을 하지 않기 때문에, 
                ## 6개 이상의 같은 돌들 중에 5개의 연결 묶음인지, 아닌지 그를 분별할 수가 없음.     
                prev_x = x - dx
                prev_y = y - dy
                if 0 <= prev_x < 19 and 0 <= prev_y < 19 and board[prev_x][prev_y] == current_stone:
                    continue
                
                # 다음 위치 계산
                next_x = x + dx
                next_y = y + dy
                # 2단계 : 한 방향으로 쭉 가면서 같은 돌 세기
                while next_x >= 0 and next_x < 19 and next_y >= 0 and next_y < 19: 
                    if board[next_x][next_y] == current_stone: 
                        stone_count += 1
                        next_x += dx
                        next_y += dy
                    else:
                       break


                if stone_count == 5:
                    ## !@##$@#$@# 5개 돌 찾고 나서 그 연속되는 방향 뒷 경로의 돌의 색깔도 확인 체크 **** 
                    ## 아래에 시작점 기준으로 5목인 순간 더이상 탐색을 하지 않기 때문에, 
                    ## 6개 이상의 같은 돌들 중에 5개의 연결 묶음인지, 아닌지 그를 분별할 수가 없음.     
                    if next_x >= 0 and next_x < 19 and next_y >= 0 and next_y < 19 and board[next_x][next_y] == current_stone:
                        continue
                    winner = current_stone
                    win_x = x+1
                    win_y = y+1
                    break  


            if winner != 0:
                break  

        
        if winner != 0:
            break  


print(winner)
if winner !=0:
    print(win_x, win_y)