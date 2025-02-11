import sys
input = sys.stdin.readline

M, n = map(int, input().split())

# 현위치 (x,y), 방향(동서남북) 
x, y = 0, 0
direction = '동'

moves = {
    '동': (1,0),
    '서': (-1,0),
    '남': (0,-1),
    '북': (0,1)
}

# Turn 0 : left_turn (왼쪽 90도 회전)
# Turn 1 : right_turn (오른쪽 90도 회전)
left_turn = {
    '동': '북',
    '북': '서',
    '서': '남',
    '남': '동'
}

right_turn = {
    '동': '남',
    '남': '서',
    '서': '북',
    '북': '동'
}

for _ in range(n):
    command, num = input().split()
    num = int(num)

    if command == 'TURN':
        if num == 0:
            direction = left_turn[direction]
        else:
            direction = right_turn[direction]
    else:
        dx,dy = moves[direction]
        new_x = x + dx*num
        new_y = y + dy*num

        if 0<= new_x <= M and 0<= new_y <= M:
            x, y = new_x, new_y
        else:
            print(-1)
            exit()

print(x,y)