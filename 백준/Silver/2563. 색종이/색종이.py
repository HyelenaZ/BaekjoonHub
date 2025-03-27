import sys
input = sys.stdin.readline

N = 100

paper = [[0] * N for _ in range(N)]
num_papers = int(input())

for _ in range(num_papers):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

area = sum(sum(row) for row in paper)

print(area)
