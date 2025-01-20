while True:
    n = int(input())

    sum = 0
    if (1<= n <= 10_000):
        for num in range(n+1):
            sum += num
        break
    else:
        int(input())
print(sum)