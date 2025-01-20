import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end =' ')
    print()