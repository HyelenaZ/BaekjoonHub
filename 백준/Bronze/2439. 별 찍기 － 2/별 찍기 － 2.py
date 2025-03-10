N = int(input().strip())

for i in range(1, N + 1):  
    print(" " * (N - i) + "*" * i)