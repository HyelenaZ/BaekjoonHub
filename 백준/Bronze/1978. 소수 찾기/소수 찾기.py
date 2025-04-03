import math
import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True 

N = int(input())
numbers = list(map(int, input().split()))  

prime_count = 0
for number in numbers:
    if is_prime(number):
        prime_count += 1

print(prime_count)
