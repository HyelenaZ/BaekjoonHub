import sys
input = sys.stdin.readline
N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_scores = [score / M * 100 for score in scores]
average = sum(new_scores) / N

print(f"{average:.6f}")