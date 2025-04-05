import math
import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

prime_lst = []

for num in range(M, N + 1):
    if is_prime(num):
        prime_lst.append(num)

if prime_lst:
    print(sum(prime_lst))  
    print(min(prime_lst))  
else:
    print(-1)
