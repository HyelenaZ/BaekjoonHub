import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    k = 0
    while 1 + 3 * k * (k + 1) < N:
        k += 1
    print(k + 1)
