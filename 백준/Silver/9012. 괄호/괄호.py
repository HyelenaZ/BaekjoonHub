import sys
input = sys.stdin.readline

def check_vps(s):
    count = 0
    for char in s.strip():
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return "NO"
    return "NO" if count else "YES"

N = int(input())
for _ in range(N):
    print(check_vps(input()))