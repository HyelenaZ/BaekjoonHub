import sys
input = sys.stdin.readline

def check_vps(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
            
    return "YES" if not stack else "NO"

N= int(input())
for _ in range(N):
    string = input().strip()
    print(check_vps(string))