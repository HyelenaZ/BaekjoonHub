import sys
input = sys.stdin.readline

T = int(input())

nums = [int(input()) for _ in range(T)]

max_n = max(nums)
is_prime = [True] * (max_n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(max_n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_n + 1, i):
            is_prime[j] = False

for n in nums:
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1
    print(count)
