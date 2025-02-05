N, M, K = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

mushroom_count = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            mushroom_count += 1

if mushroom_count == 0 or M == 0:
    print("IMPOSSIBLE")
else:
    if K == 1:
        if mushroom_count <= M:
            print("POSSIBLE")
            print(M - mushroom_count)
        else:
            print("IMPOSSIBLE")
    else:
        mushroom_cell = (mushroom_count + K - 1) // K
        if mushroom_cell <= M:
            print("POSSIBLE")
            print(M - mushroom_cell)
        else:
            print("IMPOSSIBLE")