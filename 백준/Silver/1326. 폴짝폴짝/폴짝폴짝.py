from collections import deque 

N = int(input())
stones = list(map(int, input().split()))
start, end = map(int, input().split())
record = [-1] * N  
record[start - 1] = 0
queue = deque([start - 1])

while queue:
    now = queue.popleft() 
    step = stones[now]  

    next_stone = now + step 
    while next_stone < N: 
        if record[next_stone] == -1:  
            record[next_stone] = record[now] + 1
            queue.append(next_stone) 
        next_stone += step  
    
    prev_stone = now - step
    while prev_stone >= 0:
        if record[prev_stone] == -1:
            record[prev_stone] = record[now] + 1
            queue.append(prev_stone)
        prev_stone -= step

print(record[end - 1])