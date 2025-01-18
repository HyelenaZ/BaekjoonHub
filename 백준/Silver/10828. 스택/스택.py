import sys
input = sys.stdin.readline

def process_command(command):
    if command.split()[0] == ('push'):
        stack.append(int(command.split()[1]))
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if not stack else 0)
    elif command == 'top':
        print(stack[-1] if stack else -1)

N = int(input())
stack = []

for _ in range(N):
    process_command(input().strip())