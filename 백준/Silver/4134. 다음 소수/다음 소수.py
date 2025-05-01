import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1
                
t = int(input())
for _ in range(t):
    n = int(input())
    print(next_prime(n))
