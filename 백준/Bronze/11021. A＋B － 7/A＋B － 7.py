import sys

T = int(sys.stdin.readline().strip())

for i in range(1, T + 1):  
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A + B}")