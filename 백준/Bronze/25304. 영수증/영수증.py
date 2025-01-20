import sys
input = sys.stdin.readline

def check_receipt():
    X = int(input())
    if not (1 <= X <= 1_000_000_000):
        return "No"
    
    N = int(input())
    if not (1 <= N <= 100):
        return "No"
    
    total = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if not (1 <= a <= 1_000_000 and 1 <= b <= 10):
            return "No"
        total += a*b
    
    return "Yes" if X == total else "No"

print(check_receipt())