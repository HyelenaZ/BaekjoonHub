def tile(n: int) -> int:
    MOD = 15746    
    a, b = 1, 2
    
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD
    
    return a if n == 1 else b

n = int(input())
print(tile(n))
