import sys
from bisect import bisect_left

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
trees = sorted(list(map(int, input().rstrip().split())))

def get_tree_amount(height):
    idx = bisect_left(trees, height)
    return sum(tree - height for tree in trees[idx:])

start, end = 0, trees[-1]
H = 0

while start <= end:
    current_H = (start + end) // 2
    amount = get_tree_amount(current_H)
    
    if amount >= M:
        H = current_H
        start = current_H + 1
    else:
        end = current_H - 1
print(H)