import sys
input = sys.stdin.readline

def count_changes(board, start_row, start_col, target):
    repaint_count = 0 
    
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != target[i][j]:
                repaint_count += 1
    
    return repaint_count

def min_paintings(board, n, m):
    target1 = [['W' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
    target2 = [['B' if (i + j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]
    
    min_changes = float('inf')
    for i in range(n - 7):  
        for j in range(m - 7):  
            
            changes1 = count_changes(board, i, j, target1)
            changes2 = count_changes(board, i, j, target2)
       
            min_changes = min(min_changes, changes1, changes2)
    
    return min_changes 

n, m = map(int, input().split())  
board = [input().strip() for _ in range(n)]  

print(min_paintings(board, n, m))  