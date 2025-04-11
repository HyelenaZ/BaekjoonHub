import sys
input = sys.stdin.readline

N = int(input())
x_min = float('inf') 
x_max = float('-inf')
y_min = float('inf') 
y_max = float('-inf')

for _ in range(N):
    x, y = map(int, input().split())
    x_min = min(x_min, x)
    x_max = max(x_max, x)
    y_min = min(y_min, y)
    y_max = max(y_max, y)

width = x_max - x_min
height = y_max - y_min

print(width * height)
