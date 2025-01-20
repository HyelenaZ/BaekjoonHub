import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    print(sum(list(map(int, input().split()))))