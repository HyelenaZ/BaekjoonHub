import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

min_distance = min(x, y, w - x, h - y)

print(min_distance)
