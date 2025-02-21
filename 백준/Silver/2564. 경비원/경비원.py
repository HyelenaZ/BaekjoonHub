w, h = map(int, input().split())    
store_count = int(input())           

total_len = (w + h) * 2

stores = []

for _ in range(store_count):     
    side, pos = map(int, input().split())
    if side == 1:    # 북쪽
        stores.append(pos)
    elif side == 2:  # 남쪽
        stores.append(w + h + (w - pos))
    elif side == 3:  # 서쪽
        stores.append(w + h + w + (h - pos))
    else:           # 동쪽
        stores.append(w + pos)

# 동근이 위치
dir, pos = map(int, input().split())
if dir == 1:    # 북쪽
    dk = pos                  
elif dir == 2:  # 남쪽
    dk = w + h + (w - pos)    
elif dir == 3:  # 서쪽
    dk = w + h + w + (h - pos)  
else:          # 동쪽
    dk = w + pos

# 거리 총합 계산
answer = 0
for store in stores:               
    distance1 = abs(dk - store)
    distance2 = total_len - distance1 
    answer += min(distance1, distance2)

print(answer)