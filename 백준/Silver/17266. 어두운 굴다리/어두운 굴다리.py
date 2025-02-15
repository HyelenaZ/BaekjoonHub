import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
lamp_positions = list(map(int, input().split()))

height = 1
while height <= N:
    if lamp_positions[0] - height > 0:
        height += 1
        continue
        
    if lamp_positions[-1] + height < N:
        height += 1
        continue
        
    has_dark_spot = False
    
    for i in range(M-1):
        now_lamp = lamp_positions[i]
        next_lamp = lamp_positions[i+1]
        
        now_end = now_lamp + height
        next_start = next_lamp - height
        
        if now_end < next_start:
            has_dark_spot = True
            break
            
    if has_dark_spot:
        height += 1
        continue
    
    break

print(height)