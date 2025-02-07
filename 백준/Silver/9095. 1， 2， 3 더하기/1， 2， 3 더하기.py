def count_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

T = int(input())

for _ in range(T):
    n = int(input())
    print(count_ways(n))