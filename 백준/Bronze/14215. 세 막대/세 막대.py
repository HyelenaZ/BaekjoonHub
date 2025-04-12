import sys
input = sys.stdin.readline

a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    c = a + b - 1 
    
print(a + b + c)  