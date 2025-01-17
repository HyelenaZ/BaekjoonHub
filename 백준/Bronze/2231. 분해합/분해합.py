def d(n):
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result

N = int(input())
for i in range(1, N+1):
    if d(i) == N:
        print(i)
        break
else:
    print(0)