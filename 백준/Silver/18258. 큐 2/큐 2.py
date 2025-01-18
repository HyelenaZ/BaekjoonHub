from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

def process_command(command):
    if command.startswith('push'):
        queue.append(int(command.split()[1]))
    elif command == 'pop':
        print(queue.popleft() if queue else -1) 
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(1 if not queue else 0)
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == 'back':
        print(queue[-1] if queue else -1)

N = int(input())
for _ in range(N):
    process_command(input().strip())