import sys
sys.setrecursionlimit(10000)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    world = []
    for i in range(h):
        world.append(list(map(int, input().split())))
    island = 0
    
    def find_island(a, b):
        if world[a][b] == 0:
            return
 
        world[a][b] = 0
        
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                next_a = a + x
                next_b = b + y
                
                if next_a < 0 or next_a >= h:
                    continue
                if next_b < 0 or next_b >= w:
                    continue
                    
                find_island(next_a, next_b)
    
    for i in range(h):
        for j in range(w):
            if world[i][j] == 1:
                find_island(i, j) 
                island += 1       
    
    print(island)