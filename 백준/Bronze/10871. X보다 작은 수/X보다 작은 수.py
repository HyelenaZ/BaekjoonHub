import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

for member in A:
    if member < X:
        print(member, end=' ')
