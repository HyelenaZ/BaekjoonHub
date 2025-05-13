from collections import deque

N = int(input())
line = deque(map(int, input().split()))
stack = []
current = 1

while line or stack:
    if line and line[0] == current:
        line.popleft()
        current += 1
    elif stack and stack[-1] == current:
        stack.pop()
        current += 1
    elif line:
        stack.append(line.popleft())
    else:
        break

print("Nice" if current == N + 1 else "Sad")