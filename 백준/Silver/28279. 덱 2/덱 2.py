import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N):
    command = input().split()

    if command[0] == '1':
        deq.appendleft(int(command[1]))
    elif command[0] == '2':
        deq.append(int(command[1]))
    elif command[0] == '3':
        print(deq.popleft() if deq else -1)
    elif command[0] == '4':
        print(deq.pop() if deq else -1)
    elif command[0] == '5':
        print(len(deq))
    elif command[0] == '6':
        print(1 if not deq else 0)
    elif command[0] == '7':
        print(deq[0] if deq else -1)
    elif command[0] == '8':
        print(deq[-1] if deq else -1)