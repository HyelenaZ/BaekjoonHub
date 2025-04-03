def find_kth_divisor(n, k):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    if k <= len(divisors):
        return divisors[k - 1]
    else:
        return 0

n, k = map(int, input().split())

print(find_kth_divisor(n, k))
