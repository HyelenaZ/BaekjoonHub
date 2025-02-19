from collections import deque
import sys
input = sys.stdin.readline

A, K = map(int, input().split())

queue = deque()
queue.append((A,0))
checked = set([A])

while queue:
    num, count = queue.popleft()

    if num == K:
        answer = count
        break
    next1 = num+1
    next2 = num*2

    for next_num in [next1, next2]:
        if next_num <= K and next_num not in checked:
            queue.append((next_num, count+1))
            checked.add(next_num)

print(answer)