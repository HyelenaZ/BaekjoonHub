import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

start = 0
end = max(trees)
H = 0

while start <= end:
    current_H = (start + end) //2
    
    get_tree = 0 
    for tree in trees:
        if tree > current_H:
            get_tree += tree - current_H
            if get_tree >= M:
                break
    
    if get_tree >= M:
        H = current_H
        start = current_H + 1 
    else:
        end = current_H -1

print(H)